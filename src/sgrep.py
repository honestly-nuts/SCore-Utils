#! /usr/bin/python3
import sys
import os
import re

from common import Color

def grep_file(f, token):
    text = ""
    with open(f, "r") as fl:
        for line in fl.read().split("\n"):
            for word in line.split(" "):
                if word == token:
                    text += line
                    text += "\n"
    return text

def grep_file_using_ragex(f, token):
    text = []
    col = Color()

    with open(f, "r") as fl:
        for line in fl.read().split("\n"):
            found = re.findall(token, line)
            if found:
                text.append(line[0:line.find(token)] + col.setfgcolor(token, "RED") + line[line.find(token) + len(token):])

            if len(found) >= 1:
                # buffer for add color for lines that contain same token more than once
                pass

    return text

def grep_stdin(token):

    for line in sys.stdin.read().split("\n"):
        if token in line.split(" "):
            sys.stdout.write(line + "\n")


if __name__ == '__main__':

    has_invalid_option = False
    has_exucuted_another_option = False

    # invalid args error
    if len(sys.argv) == 2:
        grep_stdin(sys.argv[1])

    elif len(sys.argv) >= 3:

        if "--help" in sys.argv:
            sys.stdout.write("No help yet, Im too la<y\n")
            sys.argv.remove("--help")

            has_exucuted_another_option = True

        elif "-E" in sys.argv:
            " for backwords compatibility "
            sys.argv.remove("-E")

        if not has_invalid_option or has_exucuted_another_option:
            for arg in sys.argv[2:]:
                if os.path.exists(arg): # no file named {} error
                    # sys.stdout.write(grep_file(arg, sys.argv[1]))
                    print("\n".join(grep_file_using_ragex(arg, sys.argv[1])))
                
        else:
            sys.exit()

    else:
        sys.stderr.write("Too few arguments!\n")
        sys.stderr.write("Usage: sgrep.py token file(s)\n")

        sys.exit()

