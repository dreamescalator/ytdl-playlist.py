# ytdl-playlist.py
A tiny automation script to download video playlists using ytdl; written in python.  

# Dependencies:
This requires having the ytdl CLI client installed.  For more information see:

https://github.com/Asecuber/ytdl

# How it works

This script reads a youtube playlist as a python dictionary stored in a text file.  Then downloads all the videos on the playlist to a destination directory of your choosing


# Usage

After downloading.  

`$ python ytdl-playlist.py dictionary.txt`

You must specify a directory where you want the downloaded videos to be saved, as well as a directory to where the dictionaries will be stored.

