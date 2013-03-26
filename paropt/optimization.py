"""Optimization functions"""

import subprocess as sp
import sys

def external_fn(cmdline_fn, performance_fn, show_iter=True):
    """Create a scipiy optimization function that calls an external program.

    Arguments:
        cmdline_fn -- A function taking a vector of parameters and returning the command line that should be called
        performance_fn -- A function taking a line of STDOUT output and returns a function value, if found, or None
    """

    it = 0

    def shell_function(x):
        """Shell function calling an external program"""

        nonlocal it

        cmdline = cmdline_fn(x)

        proc = sp.Popen(cmdline.split(' '), stdout=sp.PIPE)

        fval = None

        for line in proc.stdout:
            line = line.decode(sys.stdout.encoding)

            fval_line = performance_fn(line)
            if fval_line:
                fval = fval_line

        ret = proc.wait()

        if ret != 0:
            raise Exception("External command terminated with {} - command line: '{}'".format(ret, cmdline))

        if show_iter:
            print('{:5d} f({}) = {}'.format(it, ', '.join([ "{:.3e}".format(xv) for xv in x]) , fval ))

        it += 1

        return fval


    return shell_function
