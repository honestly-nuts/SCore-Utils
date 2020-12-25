#! /usr/bin/python3
import sys
import platform

from common import *

HELP_MESSAGE = """Usage: sarch [OPTION]...
Print machine architecture.

      --help     display this help and exit"""


def main():
    """
    The file entry point on runs (not imports).
    """
    if 1 == len(sys.argv) or FULL_ARG_PREFIX == sys.argv[1]:
        # it's important to use `platform.machine()` in order to have better support in different archs
        write_out(platform.machine())
    else:
        if "--help" in sys.argv[1:]:
            write_out(get_usage_string())
        else:  # unrecognized option
            handle_error_args()
            return 1
    return 0


if __name__ == "__main__":
    exit(main())
