import paropt.optimization
import paropt.command
import paropt.value

import paropt.neldermead
import paropt.grid

import re

import argparse
import numpy

def main():


    parser = argparse.ArgumentParser(description='Optimize a function from the command line')
    parser.add_argument('direction', choices=['min', 'max'], help='The direction of optimization (either "min" or "max")')
    parser.add_argument('fn_call', help='The system call to make to call the function with parameters, using a python format string')
    parser.add_argument('fval_regex', help='The regular expression to execute on the function\'s STDOUT stream with a capturing group representing the function value')
    parser.add_argument('-t', '--xtol', default=1e-6, type=float, help='Specify tolerance [default: %(default)s]')
    parser.add_argument('-i', '--maxiter', default=None, type=int, help='Specify maximum number of iterations [default: %(default)s]')
    parser.add_argument('-g', '--grid', dest='grid', default=False, action='store_true', help='Use grid search (requires variables to be specified as ranges)')
    parser.add_argument('-n', '--nelder-mead', dest='grid', action='store_false', help='Use nelder-mead search')

    args, ini = parser.parse_known_args()

    if len(ini) < 1:
        parser.error("Incorrect number of arguments")

    cmd = command.format_fn(args.fn_call)
    val = value.regex_fn(re.compile(args.fval_regex))

    ext = optimization.external_fn(cmd, val)

    if args.direction == 'max':
        fmin = lambda x: -ext(x)
    else:
        fmin = ext


    if args.grid:
        vardef = [parse_varrange(s) for s in ini]
        grid.minimize_grid(fmin, vardef)
    else:
        ini = [float(x) for x in ini]
        neldermead.minimize_neldermead(fmin, ini, args.xtol, args.maxiter)


def parse_varrange(s):
    """Parse a variable range definition from string"""

    is_list = s[0] == 'l'

    if is_list:
        s = s[1:]

    v = [ float(f) for f in re.split('[,;:|]', s) ]

    if is_list:
        return v

    else:

        if len(v) == 1:
            return [v[0]]

        elif len(v) == 2:
            return numpy.arange(v[0], v[1], 1)

        elif len(v) == 3:
            return numpy.arange(v[0], v[1], v[2])

        else:
            raise Exception("Unknown number range format: '{}'".format(s))

