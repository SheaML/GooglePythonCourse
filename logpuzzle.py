#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib
import urllib.request

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
filename='/home/shea/Downloads/google-python-exercises/logpuzzle/place_code.google.com'

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  
  host='http://' + filename.split('_')[-1]
  text=open(filename).read()
  results=re.findall("[^ ]+puzzle[^ ]+",text)
  results=sorted(set(results))
  return [host+i for i in results]
  
  

def download_images(img_urls, dest_dir):
  """
  Given the urls already in the correct order, downloads
  each image into the given directory.
  
  Gives the images local filenames img0, img1, and so on.
  
  Creates an index.html in the directory
  with an img tag to show each local image file.
  
  Creates the directory if necessary.
  """
  
  if os.path.exists(dest_dir) == False:
    os.mkdir(dest_dir)

  srcstring=""
  for url in img_urls:
    # Split on the rightmost / and take everything on the right side of that
    name = os.path.basename(url)

    # Combine the name and the downloads directory to get the local filename
    filename = os.path.join(dest_dir, name)

    # Download the file if it does not exist
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename)

    substring=f'<img src="{url}">'
    srcstring = srcstring + substring
    
    outfile='index.html'
    with open(outfile,'w') as out:
        out.writelines(['<verbatim>','<html>','<body>',srcstring,'</body>','</html>'])

def main():
  args = sys.argv[1:]

  if not args:
    print('usage: [--todir dir] logfile ')
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print('\n'.join(img_urls))

if __name__ == '__main__':
  main()
