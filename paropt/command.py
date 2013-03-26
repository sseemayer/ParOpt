"""Command functions for use with external optimization functions"""

def format_fn(frmat):
    """Create a commandline function that builds a command line from a format string

    Upon binding on parameters, String.format will be called to create a command line call.

    Example:

    >>> fn = format_fn("echo {1} {0}")
    >>> fn(["World", "Hello"])
    'echo Hello World'

    """

    def inner(xval):
        """Inner command line funtion"""

        try:
            return frmat.format(*xval)
        except IndexError:
            raise Exception("Format string has more fields than variables!")

    return inner

