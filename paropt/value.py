"""Functions for parsing the function value from external commands"""

import re

def regex_fn(pattern, process_fn=float):
    """Parse a command's output using a regular expression.

    Arguments:
    pattern -- The pattern to match against, containing a capturing group that matches to the value
    process_fn -- The optional function that will be used to process the matching group into a numeric value

    Example:

    >>> fn = regex_fn(r'final fx = (.*)')
    >>> fn('final fx')
    >>> fn('final fx = 123.4')
    123.4

    """

    # if we are passed a string, compile it to a RegexObject
    if isinstance(pattern, str):
        pattern = re.compile(pattern)

    def inside(line):
        """Inner matching function"""
        m = pattern.search(line)
        if m:
            return process_fn(m.group(1))
        else:
            return None

    return inside
