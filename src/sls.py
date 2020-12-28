#! /usr/bin/python3
import sys
import os
from common import Color

def listDir(root, dirColor="BLUE", fileColor="BROWN"):
    listing = []
    col = Color()
    
    for content in os.listdir(root):
        if os.path.isdir(content):
            listing.append(col.setfgcolor(content, dirColor))
        else:
            listing.append(col.setfgcolor(content, fileColor))

    return listing

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.stdout.write("  ".join(listDir("./", "BLUE", "GREEN")) + "\n")
    else:
        if os.path.isdir(sys.argv[1]):
            sys.stdout.write("  ".join(listDir(sys.argv[1], "BLUE", "GREEN")) + "\n")
        else:
            sys.stderr.write(f"{sys.argv[1]} is not a directory\n")
            sys.exit()
