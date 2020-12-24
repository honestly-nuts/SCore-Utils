#! /usr/bin/python3
import sys
import platform

from common import *

HELP_MESSAGE = """Usage: suname [OPTION]...
Print certain system information.  With no OPTION, same as -s.

  -a, --all                print all information, in the following order,
                             except omit -p and -i if unknown:
  -s, --kernel-name        print the kernel name
  -n, --nodename           print the network node hostname
  -r, --kernel-release     print the kernel release
  -v, --kernel-version     print the kernel version
  -m, --machine            print the machine hardware name
  -p, --processor          print the processor type (non-portable)
  -i, --hardware-platform  print the hardware platform (non-portable)
      --help     display this help and exit"""


def get_full_uname():
    """
    Returns full uname, of all options omitting -p and -i if unknown.
    """
    return " ".join(list(platform.uname()))


def main():
    success = False

    if 1 == len(sys.argv):
        write_out(platform.system())
        return 0

    if "--help" in sys.argv[1:]:
        write_out(HELP_MESSAGE)
        return 0

    if "-a" in sys.argv[1:]:
        write_out(get_full_uname())
        return 0

    if FULL_ARG_PREFIX == sys.argv[1]:
        if 2 == len(sys.argv):
            write_out(platform.system())
            return 0
        else:
            handle_error_args()
            return 1

    if "-s" in sys.argv[1:] or "--kernel-name" in sys.argv[1:]:
        write_out(platform.system(), end=" ")
        success = True

    if "-n" in sys.argv[1:] or "--nodename" in sys.argv[1:]:
        write_out(platform.node(), end=" ")
        success = True

    if "-r" in sys.argv[1:] or "--kernel-release" in sys.argv[1:]:
        write_out(plaform.release(), end=" ")
        success = True

    if "-v" in sys.argv[1:] or "--kernel-version" in sys.argv[1:]:
        write_out(platform.version(), end=" ")
        success = True

    if "-m" in sys.argv[1:] or "--machine" in sys.argv[1:]:
        write_out(platform.machine(), end=" ")
        success = True

    if "-p" in sys.argv[1:] or "--processor" in sys.argv[1:]:
        write_out(platform.processor(), end=" ")
        success = True

    if "-i" in sys.argv[1:] or "--hardware-platform" in sys.argv[1:]:
        write_out(platform.machine(), end=" ")
        success = True

    if success:
        write_out("")  # to add the newline

    else:  # handle errors
        handle_error_args() 
        return 1
    
    return 0


if __name__ == '__main__':
    exit(main())
