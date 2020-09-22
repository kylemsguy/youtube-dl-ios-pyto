import console
import sys
import glob
import os
from youtube_dl import YoutubeDL

if len(sys.argv) != 2:
	raise IndexError('usage: %s url;type' % (sys.argv[0]))
url = sys.argv[1]
#dl_type = sys.argv[2]
print('url: %s' % (url))
quit()

choices = (
	('Audio', 'bestaudio[ext=m4a]', 'm4a'),
	('Video', 'best[ext=mp4]', 'mp4'),
)
#choice = console.alert('youtube-dl', 'Version to extract:',
#	*(c[0] for c in choices))

#choice = choices[0] if dl_type == "audio"
choice = None

_, format, ext = choices[choice-1]
print('format: %s' % (format))

opts = {
	'format': format
}
with YoutubeDL(opts) as ydl:
	ydl.download([url])

file = max(glob.glob('*.'+ext), key=os.path.getctime)
if not file:
	raise IndexError('downloaded file not found')
print('downloaded: %s' % (file))

try:
	console.open_in(file)	
finally:
	os.remove(file)
	print('deleted: %s' % (file))
