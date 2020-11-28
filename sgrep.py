#! /bin/python3.8
import sys
import re

if len(sys.argv) < 3:
    print("Usage: sgrep.py token file(s)")
    sys.exit()

def grep(token):
    text = ""
    for i in sys.argv[2:]:
        with open(i, "r") as fl:
            for line in fl.read().split("\n"):
                for word in line.split(' '):
                    if word == token:
                        text += line
    return text

print(grep(sys.argv[1]))
