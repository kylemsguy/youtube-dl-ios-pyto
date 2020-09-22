# youtube-dl-ios

> [youtube-dl][youtube-dl] for iOS, with [Pyto](pyto) and
[Shortcuts][shortcuts]

Download a video (or its audio track) by sharing it to a shortcut

The shortcut calls a helper script run within Pythonista. This script passes the
URL to youtube-dl to do the actual download. After the download completes, it's 
stored in the same directory as your original script, and can be copied to any app, 
such as VLC.

## Install

1. Install [Pyto](https://pyto.app/)
2. Download ytdl.py to where you want the videos to be saved to in Files (e.g. On Your iPhone -> Downloads)
3. Run the script once (it will error out, but this is important later)
3. Install the shortcut: [iCloud link][shortcut]
4. Modify the "Run script" action to point to ytdl.py, if it isn't already (if you did 3, it should show up in the list)

## Usage

1. Share a video to Shortcuts and then youtube-dl-ios-pyto
2. The downloaded file is saved 
3. (If the download is interrupted, either repeat 1-2 to resume, or delete the .part files from Files)

[youtube-dl]: https://rg3.github.io/youtube-dl/
[pyto]: https://pyto.app/
[shortcuts]: https://support.apple.com/en-jo/guide/shortcuts/welcome/ios
[shortcut]: https://www.icloud.com/shortcuts/7d9df040c0d94893b47dd6a9e449c480
