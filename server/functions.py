from pytube import YouTube

# Get Video details
def getMedia(url):
    try:
        yt = YouTube(url)
        video = {
            'title': yt.title,
            'length': yt.length,
            'thumbnail_url': yt.thumbnail_url,
            'resolution': sorted(list(set([stream.resolution for stream in yt.streams if stream.resolution])), key = lambda resolution: int(resolution[0:-1])),
        }
        return video
    except:
        # When a URL is invalid
        return {}
    
# Download a video
def downloadVideo(url, resolution):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(res=resolution).first()

        if stream:
            stream.download(output_path="C:/Users/USER/Downloads/")

    except Exception as e:
        print(f'Error while downloading video', e)



