#!/usr/bin/python

import subprocess, sys, requests, unicodedata, re, argparse, os
from bs4 import BeautifulSoup

#HELPER FUNCTIONS:
def sanitize(string):
        s = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore')
        return "".join(s.split())

def build(k, v, folder):        
        v = str(folder) + str(v) + ".flv"
        k = re.search('^(.*?)&', k).group(1)
        return "ytdl " + "https://youtube.com" + str(k)+ " > " + v[2:]

# Dict example:
# {'url':'video title'}
def dictfile(_playlist):
        _playlist = dict_dir + str(_file)
        with open(_playlist) as f:
                return eval(f.read())

def new_folder(_name):
        _new_folder = os.path.join(os.getcwd, _name)
        if not os.path.isdir(_new_folder): os.makedirs(_new_folder)
        return _new_folder

#PACKAGE FUNCTIONS
def playlist(_url):
        _playlist_dict = {}
        soup = BeautifulSoup(requests.get(_url).text)
        for a in soup.find_all("a"):
                if "watch" in a.attrs.get('href'):
                        _playlist_dict[a.attrs.get('href')] = sanitize(a.text)
        return _playlist_dict
                        

def download(_playlist, *path):
        if path: f= path[0]
        else : f = ""
        for k, v in _playlist.iteritems():
                proc = subprocess.Popen([build(k, v, f)], shell=True)
                proc.wait()
        
#ARGPARSING
parser = argparse.ArgumentParser()

#Example:
#./playlist.py -p "path/to/playlist" -l "https://www.youtube.com/playlist?list=PLUl4u3cNGP63w3DE9izYp_3fpAdi0Wkga"
parser.add_argument("-l", "--link", type=str, help="a link to a youtube playlist")
parser.add_argument("-d", "--dict", type=str, help="path to a text file containing a python dictionary")
parser.add_argument("-f", "--folder",  type=str, help="path where you want your playlist downloaded")
args = parser.parse_args()

if args.link: download(playlist(args.link))
if args.dict: download(dictfile(args.dict))
if args.folder:
        if args.link or args.file:
                if args.folder:
                        download(playlist(args.link), new_folder(args.folder))

