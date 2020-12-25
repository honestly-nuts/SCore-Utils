import sys
import os.path
import inspect

FULL_ARG_PREFIX = "--"
SHORT_ARG_PREFIX = "-"


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


def handle_error_args(arg_list: list = sys.argv[1:]):
    """
    An implementation of basic error handling to print the correct error message for each case.
    :param arg_list: list of arguments (not including the file name)
    """
    command_name = _get_command_name()
    
    if 0 == len(arg_list):  # nothing to handle
        return

    if arg_list[0].startswith(FULL_ARG_PREFIX):
        write_out(f"{command_name}: unrecognized option '{arg_list[0]}'")
    elif arg_list[0].startswith("-") and SHORT_ARG_PREFIX != arg_list[0]:
        write_out(f"{command_name}: invalid option -- '{arg_list[0][1:]}'")
    else:
        write_out(f"{command_name}: extra operand '{arg_list[0]}'")
    write_out(f"Try '{command_name} --help' for more information.")
