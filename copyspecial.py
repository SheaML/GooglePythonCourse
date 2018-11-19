#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess
from subprocess import PIPE

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them

def printdir(direc):
  filenames = os.listdir(direc)
  files=[]
  for filename in filenames:
      if re.search("__\w+__",filename):
          files.append(os.path.abspath(os.path.join(direc, filename)))
  return files

def copylist(files,path):
    if os.path.exists(path) == False:
        os.mkdir(path)
    for i in files[0]:
        shutil.copy(i,path)
    
def ziplist(files,zfile):
    command = ['zip',zfile] + files[0]
    result = subprocess.run(command,stdout=PIPE,stderr=PIPE)
    print(result.returncode, result.stdout, result.stderr)
    
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  files=[]
  for i in args:
    files.append(printdir(i))
  #print(files)

  copylist(files,todir)
  ziplist(files,tozip)

    
if __name__ == "__main__":
  main()
