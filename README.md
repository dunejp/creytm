> [!IMPORTANT]
> **creytm** has been deprecated due to PyTube's bug.
> 
> However, you can use **creytm-piped-v2** as an alternative.

## :minidisc: creytm
An oversimplified MPEG-3 downloader for YouTube videos. <br>
[Try a demo](https://creytm.vercel.app/3BFTio5296w/you-got-rickrolled-by-an-api.mp3)

## :books: Usage
```html
<audio src="https://creytm.vercel.app/YT-VIDEO-ID"></audio>
```

> [!IMPORTANT]
> Do not include parameters (especially `?si=...`), hashes, and `/` at the end of the URL.

### :file_folder: With custom file name (optional)

```html
<p>Try downloading the audio</p>
<audio src="https://creytm.vercel.app/YT-VIDEO-ID/Your-File-Name.mp3" controls=""></audio>
```

### :scroll: Recommended usage

For downloading audio, it is **NOT** recommended to use the music videos.

1. Use a video with `- Topic` in its author name
2. If none, use a video with `(Audio)` or `(Official Audio)` in its title
3. If none, use a visualizer that don't heavily animate its frames.


### :lady_beetle: Issue with YT Music

Since this API focuses on `youtube`, some of the `music.youtube` files are undetectable.

If possible, use a video that can be found on `m.youtube.com`.

## :construction: Limit

|   | Recommended | Somehow works | Will not work |
|:-:|:-:|:-:|:-:|
| **Duration** | 5 minutes and below | 6 minutes to 12 minutes | 13 minutes and above |
| **Size** | 1MB and below | 2MB to 3MB | 4MB above |

## :hourglass_flowing_sand: Latency

| Duration | Latency |
|:--------:|:-------:|
| 1-7 minutes | 1-3 seconds |
| 7-10 minutes | 2-5 seconds |
| 10+ minutes | 4-7+ seconds (prediction) |

<img src="https://komarev.com/ghpvc/?username=creuserr" alt="" width="0"></img>
