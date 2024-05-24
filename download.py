from pytube import YouTube
from http.server import BaseHTTPRequestHandler
from pytube.cipher import get_throttling_function_code
import re
import mock

def patched_throttling_plan(js: str):
  raw_code = get_throttling_function_code(js)
  transform_start = r"try{"
  plan_regex = re.compile(transform_start)
  match = plan_regex.search(raw_code)
  transform_plan_raw = js
  step_start = r"c\[(\d+)\]\(c\[(\d+)\](,c(\[(\d+)\]))?\)"
  step_regex = re.compile(step_start)
  matches = step_regex.findall(transform_plan_raw)
  transform_steps = []
  for match in matches:
    if match[4] != '':
      transform_steps.append((match[0],match[1],match[4]))
    else:
      transform_steps.append((match[0],match[1]))
  return transform_steps

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    if len(self.path) < 2:
      return self.end('400 Bad Request: Incomplete Parameter', 400)
    if self.path == '/favicon.ico':
      self.send_response(302)
      self.send_header('Location', 'https://m.youtube.com/favicon.ico')
      return self.end_headers()
    try:
      with mock.patch('pytube.cipher.get_throttling_plan', patched_throttling_plan):
        video = YouTube('https://youtu.be' + self.path)
        stream = video.streams.filter(only_audio=True).first()
        stream.download(filename='output.mp3', output_path='/tmp/')
        self.send_response(200)
        self.send_header('Content-type', 'audio/mp3')
        self.end_headers()
        with open('/tmp/output.mp3', 'rb') as f:
          self.wfile.write(f.read())
          return f.close()
    except Exception as e:
      if('regex_search' in str(e)):
        return self.end('400 Bad Request: Invalid Parameter', 400)
      if('unavailable' in str(e)):
        return self.end('404 Not Found: Unavailable', 404)
      return self.end('500 Internal Error: ' + str(e), 500)
  def end(self, text, status):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))