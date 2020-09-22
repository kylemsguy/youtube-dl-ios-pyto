#import console
import sys
import glob
import os
import json
from youtube_dl import YoutubeDL

"""
Input format: (JSON)
argv[1] = {"url": "<YOUTUBE_URL>", "type": "<TYPE>"}
"""

if len(sys.argv) != 2:
    raise IndexError('usage: %s data_as_json' % (sys.argv[0]))

input_data = json.loads(sys.argv[1])
url = input_data['url']
dl_type = input_data['type']
print('input: %s' % (input_data))

choices = {
    'audio': ('bestaudio[ext=m4a]', 'm4a'),
    'video': ('best[ext=mp4]', 'mp4'),
}

fmt, ext = choices[dl_type]
print('format: %s' % (fmt))

opts = {
    'format': fmt,
}
with YoutubeDL(opts) as ydl:
    ydl.download([url])

f = max(glob.glob('*.'+ext), key=os.path.getctime)
if not f:
    raise IndexError('downloaded file not found')
print('downloaded: %s' % (f))

try:
    print("File successfully downloaded {f}".format(f=f))
    #console.open_in(file)	
finally:
    os.remove(f)
    print('deleted: %s' % (f))
