# My Youtube Channel

Posted: Tue, 17-11-2024.

I made a youtube channel and posted my first video.
Link [here](https://www.youtube.com/@jonesangga).
I always fail to verify my phone number.
So I cannot post videos longer than 15 minutes for now.

My first video is about creating a vim plugin [fsticky](https://codeberg.org/jonesangga/fsticky/).
I recorded with obs-studio and then reduced the file size using ffmpeg with the following command
```
ffmpeg -i input.mp4 -vcodec libx264 -crf 24 output.mp4
```

This is not intended as tutorial.
I just record what I think interesting.
I don't record with my own voice because my pronounciation is bad.
Also I don't have a good setup for recording audio.
But I will use text to speech voice.
The one I use is [piper](https://github.com/rhasspy/piper).
a fast, local neural text to speech system.
Actually this is what my next video about. I will write a wrapper
around piper. So I can call that inside vim and passing curently selected
text to say.
