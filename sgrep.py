#! /bin/python3.8
import sys
import re


def grep_file(f, token):
    text = ""
    with open(f, "r") as fl:
        for line in fl.read().split("\n"):
            for word in line.split(" "):
                if word == token:
                    text += line
    return text

def grep_stdin(token):
    for line in sys.stdin.read().split("\n"):
        if token in line.split(" "):
            sys.stdout.write(line + "\n")


if __name__ == '__main__':
    optlist = []

    if len(sys.argv) == 2:
        grep_stdin(sys.argv[1])
    elif len(sys.argv) >= 3:
        text = ""
        for arg in sys.argv[1:]:
            if re.findall(r"^-", arg) != []:
                optlist.append(arg)

        # to desable the options when executed once
        n_opt_defuse = False

        for arg in sys.argv[2:]:
            if optlist != [] and arg not in optlist:
                text += grep_file(arg, sys.argv[1])
                if "-c" in optlist:
                    print(len(text.split("\n")))
                    n_opt_defuse = True
                else:
                    sys.stderr.write("Option not found\n")
                    sys.exit()

            elif optlist == []:
                sys.stdout.write(grep_file(arg, sys.argv[1]))

    else:
        sys.stderr.write("Too few arguments!\n")
        sys.stderr.write("Usage: sgrep.py token file(s)\n")
        sys.exit()

