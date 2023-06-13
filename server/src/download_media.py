from pytube import YouTube

from src.image_encoding import encode_image_to_base_64

def downloadMedia(url):
    try:
        yt = YouTube(url)
        video = {
            'title': yt.title,
            'length': yt.length,
            'thumbnail_url': yt.thumbnail_url,
        }
        return video
    except:
        # When a URL is invalid
        return {}
    


