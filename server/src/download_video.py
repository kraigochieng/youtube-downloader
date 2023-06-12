from pytube import YouTube


def downloadVideo(url):
    yt = YouTube(url)
    video = {
        'title': yt.title,
        'full_length': yt.length,
    }
    return video


