#! /usr/bin/python3
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
        if "append" in options["oflag"] or "notrunc" in options["conv"]:
            write_mode = "wb+"
        else:
            write_mode = "ab"
        output_file = open(options["of"], write_mode, buffering=0)
    else:
        output_file = sys.stdout

    if options["bs"] != 512:
        in_bytes = options["bs"]
        out_bytes = options["bs"]
    else:
        in_bytes = options["ibs"]
        out_bytes = options["obs"]

    if "skip_bytes" in options["iflag"]:
        in_seek = options["skip"]
    else:
        in_seek = options["skip"] * in_bytes
    input_file.seek(in_seek)

    if "seek_bytes" in options["oflag"]:
        out_seek = options["seek"]
    else:
        out_seek = options["seek"] * in_bytes

    if output_file.seekable():
        output_file.seek(out_seek)
    else:
        output_file.write("\0" * out_seek)

    if options["count"]:
        if "count_bytes" in options["oflag"]:
            count = options["count"]
            while count > in_bytes:
                data = input_file.read(in_bytes)
                output_file.write(data)
            data = input_file.read(count)
            output_file.write(data)
        else:
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
