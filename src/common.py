import sys
import os.path
import inspect

FULL_ARG_PREFIX = "--"
SHORT_ARG_PREFIX = "-"

class Color:
    def __init__(self):
        self.FGCOLORS = {
            "BLACK" : "\033[0;30m",
            "RED" : "\033[0;31m",
            "GREEN" : "\033[0;32m",
            "BROWN" : "\033[0;33m",
            "BLUE" : "\033[0;34m",
            "ENDSTYLE" : "\033[0m"
        }

    # if you don't know what : str means then it means that the argument passed should be a str else raise an erro.
    def setfgcolor(self, text : str, colorName : str):
        return self.FGCOLORS[colorName] + text + self.FGCOLORS["ENDSTYLE"]

def _get_command_name() -> str:
    """
    This is a special utility function. 
    since it should only be called in `handle_errors`, it goes 3 calls up to call chain:
    current->handle_errors->`caller function` and retrieves the file name from there.
    afterwards, it removes the `.py` extension and the prefixes to the filename.
    """
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe)
    return os.path.splitext(os.path.basename(calframe[2].filename))[0]


def exit(exit_code):
    """
    Makes sure all information was flushed to stdout and stderr, then exits.
    """
    sys.stdout.flush()
    sys.stderr.flush()
    sys.exit(exit_code)


def write_out(string: str, end: str = "\n"):
    """
    Writes the given string and end to stdout, then flushes.
    """
    sys.stdout.write(string)
    sys.stdout.write(end)
    sys.stdout.flush()


def write_err(string: str, end: str = "\n"):
    """
    Writes the given string and end to stderr, then flushes.
    """
    sys.stderr.write(string)
    sys.stderr.write(end)
    sys.stderr.flush()
