from pytube import YouTube
print('Welcome to the free youtube videos and audio downloader.')
url = input('please paste your youtube video url here : ')
my_video = YouTube(url)
print(my_video.title)#show title
print(my_video.streams.first().download()) #mp4