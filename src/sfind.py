#!/usr/bin/python3

import sys
import os
import re

def find(token, return_str=False, return_token=''):
    text = []
    for root, dirs, files in os.walk("/"):
        all_content = dirs + files # To search the token in one for loop

        for name in all_content:
            if re.findall(token, name):
                text.append(os.path.join(root, name))

    if return_str:
        if return_token == '':
            return "\n".join(text)
        else:
            return return_token.join(text)
    else:
        return text

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Too few arguments!\n")
        sys.exit()

    find(sys.argv[1], True)
