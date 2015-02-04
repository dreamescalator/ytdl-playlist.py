#!/usr/bin/env python

import subprocess
import sys

playlist = str(sys.argv[1])
dict_dir = "/path/to/python/dictionaries/"
dest_dir = "/path/to/downlaoded/videos/"

def to_dict(_playlist):
        _playlist = dict_dir + str(_file)
        with open(_playlist) as f:
                return eval(f.read())

def download(_playlist):
        _playlist = to_dict(_playlist)
        for k, v in _playlist.iteritems():
                v = str(v)+".flv"
                sh = "ytdl "+str(k)+" > "+ dest_dir + v
                proc = subprocess.Popen([sh], shell=True)
                proc.wait()

download(playlist)

