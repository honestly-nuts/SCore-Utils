#! /usr/bin/python3
import sys
import platform


def get_version_string():
    """
    Returns the version string.
    """
    return "sarch 1.0.0\n"


def get_usage_string():
    """
    Returns the usage string.
    """
    # this isn't a pretty string, but this way it is the easiest to understand how it will look in a terminal
    return """Usage: sarch [OPTION]...
Print machine architecture.

      --help     display this help and exit
      --version  output version information and exit\n"""


def main():
    """
    The file entry point on runs (not imports).
    """
    if 1 == len(sys.argv):
        # it's important to use `platform.machine()` in order to have better support in different archs
        sys.stdout.write(platform.machine())
    else:
        if "--help" in sys.argv[1:]:
            sys.stdout.write(get_usage_string())
        elif "--version" in sys.argv[1:]:
            sys.stdout.write(get_version_string())
        else:  # unrecognized option
            sys.stderr.write(f"sarch: extra operand {sys.argv[1]}\n"
                             f"Try 'sarch --help' for more information.\n")


if __name__ == "__main__":
    main()
