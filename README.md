## creytm
An oversimplified and unauthorized MPEG-3 downloader for YouTube videos. [Try a demo](https://creytm.vercel.app/aPnqx56V8-0)

### Usage
```html
<audio src="https://creytm.vercel.app/YT-VIDEO-ID"></audio>
```

> [!IMPORTANT]
> Do not include parameters (especially `?si=...`), hashes, and `/` at the end of the URL.

#### With custom file name (optional)

```html
<audio src="https://creytm.vercel.app/YT-VIDEO-ID/Your-File-Name.mp3" controls=""></audio>
```

#### Recommended usage

For downloading audio, it is recommended to **not** use the music videos, visualizers, lyric videos (both official and unofficial).

1. Use a video with `- Topic` in its author name
2. If none, use a video with `(Audio)` or `(Official Audio)` in its title
3. If none, use a visualizer that don't heavily animate its frames.


#### Known `music.youtube` issue

Since this API focuses on `youtube`, some of the `music.youtube` files are undetectable.

If possible, use a video that can be found on `m.youtube.com`.

#### Limit

|   | Recommended | Somehow works | Will not work |
|:-:|:-:|:-:|:-:|
| **Duration** | 5 minutes and below | 6 minutes to 12 minutes | 13 minutes and above |
| **Size** | 1MB and below | 2MB to 3MB | 4MB above |

### Latency

| Duration | Latency |
|:--------:|:-------:|
| 1-7 minutes | 1-3 seconds |
| 7-10 minutes | 2-5 seconds |
| 10+ minutes | 4-7+ seconds (prediction) |
