from pytube import YouTube

video = YouTube(" https://www.youtube.com/watch?v=7oMNqAE_OVE")

vid= video.streams.get_highest_resolution()

vid.download('Musique')