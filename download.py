import yt_dlp
import re
import os



def downloadvideosfromchannel(url, videodir):
    # ℹ️ See help(yt_dlp.YoutubeDL) for a list of available options and public functions
    ydl_opts = {
        'outtmpl': videodir+'/%(id)s'+'.mp4',
        'format': 'best',
        'writedescription':True,
        'verbose': True,
        'writethumbnail': True, # Required to embed thumbnail
        'proxy': 'socks5://127.0.0.1:1080'
    }
 
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # info = ydl.extract_info(url, download=True)
        err=ydl.download(url)
with open('urls.txt','r') as f:
    urls=f.read()
urls=urls.split(',')
for url in urls:
    url='https://www.tiktok.com/@capcut/video/'+url.replace("'",'').strip()
    print(url)
    downloadvideosfromchannel(url, './videos')



