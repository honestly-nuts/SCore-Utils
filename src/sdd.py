#!/bin/python3.8
import sys


def usage():
    print(
        """Usage: sdd [options]
    Copies a file converting and formatting it according to the options.
    Options:
        bs=BYTES        read and write up to BYTES bytes at a time (default: 512);
                        overrides ibs and obs
        cbs=BYTES       convert BYTES bytes at a time
        conv=CONVS      convert the file as per the comma separated symbol list
        count=N         copy only N input blocks
        ibs=BYTES       read up to BYTES bytes at a time (default: 512)
        if=FILE         read from FILE instead of stdin
        iflag=FLAGS     read as per the comma separated symbol list
        obs=BYTES       write BYTES bytes at a time (default: 512)
        of=FILE         write to FILE instead of stdout
        oflag=FLAGS     write as per the comma separated symbol list
        seek=N          skip N obs-sized blocks at start of output
        skip=N          skip N ibs-sized blocks at start of input"""
    )


def convert_file(options):
    pass


if __name__ == "__main__":
    options = {
        "bs": 512,
        "cbs": 512,
        "conv": [],
        "count": 0,
        "ibs": 512,
        "if": "",
        "iflag": [],
        "obs": 512,
        "of": "",
        "oflag": [],
        "seek": 0,
        "skip": 0,
    }

    index = 1
    while index < len(sys.argv):
        if "conv" in sys.argv[index]:
            _, flag = sys.argv[index].split("=")
            flags = [flag.strip(",")]
            index += 1
            while index < len(sys.argv) and "=" not in sys.argv:
                flags.append(sys.argv[index].strip(","))
            options["conv"] = flags

        elif "iflag" in sys.argv[index]:
            _, flag = sys.argv[index].split("=")
            flags = [flag.strip(",")]
            index += 1
            while index < len(sys.argv) and "=" not in sys.argv:
                flags.append(sys.argv[index].strip(","))
            options["iflag"] = flags

        elif "oflag" in sys.argv[index]:
            _, flag = sys.argv[index].split("=")
            flags = [flag.strip(",")]
            index += 1
            while index < len(sys.argv) and "=" not in sys.argv:
                flags.append(sys.argv[index].strip(","))
            options["oflag"] = flags

        elif "=" in sys.argv[index]:
            option, value = sys.argv[index].split("=")
            options[option] = value
        index += 1

        convert_file(options)
