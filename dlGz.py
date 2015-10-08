#!/usr/bin/env python
#! -*- coding: utf-8 -*-
import sys, os, urllib, gzip

def GetAndGzip(url, outFile):
    remote = urllib.urlopen(url).read()
    gzfile = gzip.GzipFile(filename='', mode='wb', fileobj=outFile)
    gzfile.write(remote)
    gzfile.close()

if len(sys.argv) <> 2:
    print '使いかた: python wgetgz.py url'
else:
    url = sys.argv[1]
    GetAndGzip(url, sys.stdout)
