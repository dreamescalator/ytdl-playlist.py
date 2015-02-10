# ytdl-playlist.py
A tiny automation script to download video playlists using ytdl; written in python.  

# Dependencies:
This requires having the ytdl CLI client installed.  For more information see:

https://github.com/Asecuber/ytdl

Python module dependencies:
beautifulsoup4: http://www.crummy.com/software/BeautifulSoup/
requests: http://docs.python-requests.org/en/latest/
which can be installed with pip: https://pypi.python.org/pypi/pip/6.0.6

# How it works
This script downloads all the videos on the playlist to a destination directory of your choosing, if none specified it will just download the playlist videos to a CWD


# Set-up
1) download this git repo
2) Install ytdl CLI client and all the required Python dependecies
3) $ cd ytdl-playlist.py && [sudo] chmod 755 playlist.py

# Usage


$ ./playlist.py -l  "https://www.youtube.com/playlist?list=PLUl4u3cNGP63w3DE9izYp_3fpAdi0Wkga" 

OR

$ ./playlist.py -l  /path/to/my/dictfile.txt



# Optional Arguments

-h = help menu/list of commands
-p = path to target directory to save playlist videos

$ ./playlist.py -l  "https://www.youtube.com/playlist?list=PLUl4u3cNGP63w3DE9izYp_3fpAdi0Wkga" -p /path/where/I/want/to/save/videos

(Note:, if the path or folder doesnt exist, it will be created for you)








You must specify a directory where you want the downloaded videos to be saved, as well as a directory to where the dictionaries will be stored.

