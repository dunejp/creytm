from pytube import YouTube
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    if 'id' not in self.query:
      return end('400 Bad Request: Incomplete Parameter', 400)
    try:
      video = YouTube('https://youtu.be/' + self.query['id'])
      stream = video.streams.filter(only_audio=True).first()
      stream.download(filename='output.mp3', output_path='/tmp/')
      self.send_response(200)
      self.send_header('Content-type', 'audio/mp3')
      self.end_headers()
      with open('/tmp/', 'rb') as f:
        self.wfile.write(f.read())
        return f.close()
    except Exception as e:
      return end('500 Internal Error: ' + str(e), 500)
  def end(self, text, status):
    self.send_response(status)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(text.encode('utf-8'))
