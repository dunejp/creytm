## creytm
An oversimplified and unauthorized MPEG-3 downloader for YouTube videos. [Try a demo](https://creytm.vercel.app/aPnqx56V8-0)

### Usage
```http
GET https://creytm.vercel.app/<YT-VIDEO-ID>
```

> [!IMPORTANT]
> Do not include parameters (especially `?si=...`), hashes, and `/` at the end of the URL.

### Latency

| Duration | Latency |
|:--------:|:-------:|
| 1-7 minutes | 1-3 seconds |
| 7-10 minutes | 2-5 seconds |
| 10+ minutes | 4-7+ seconds (prediction) |
