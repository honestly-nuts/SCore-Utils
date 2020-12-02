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
    if options["if"]:
        # TODO: iflags support
        input_file = open(options["if"], "rb", buffering=0)
    else:
        input_file = sys.stdin

    if options["of"]:
        # TODO: oflags support
        output_file = open(options["of"], "wb", buffering=0)
    else:
        output_file = sys.stdout

    if options["bs"] != 512:
        in_bytes = options["bs"]
        out_bytes = options["bs"]
    else:
        in_bytes = options["ibs"]
        out_bytes = options["obs"]

    input_file.seek(options["skip"])
    if output_file.seekable():
        output_file.seek(options["seek"])
    else:
        output_file.write("\0" * options["seek"])

    if options["count"]:
        for _ in range(options["count"]):
            data = input_file.read(in_bytes)
            output_file.write(data)
    else:
        while data := input_file.read(in_bytes):
            while data:
                segment = data[:out_bytes]
                output_file.write(segment)
                data = data[out_bytes:]


if __name__ == "__main__":
    # Default options
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

    # Parse sys.argv
    index = 1
    while index < len(sys.argv):
        if "conv" in sys.argv[index]:
            _, flag = sys.argv[index].split("=")
            flags = [flag.strip(",")]
            index += 1
            while index < len(sys.argv) and "," in sys.argv[index]:
                flags.append(sys.argv[index].strip(","))
            options["conv"] = flags

        elif "iflag" in sys.argv[index]:
            _, flag = sys.argv[index].split("=")
            flags = [flag.strip(",")]
            index += 1
            while index < len(sys.argv) and "," in sys.argv[index]:
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
