import paropt.optimization
import paropt.command
import paropt.value
import re
from scipy.optimize import minimize

import argparse

def main():


    parser = argparse.ArgumentParser(description='Optimize a function from the command line')
    parser.add_argument('direction', choices=['min', 'max'], help='The direction of optimization (either "min" or "max")')
    parser.add_argument('fn_call', help='The system call to make to call the function with parameters, using a python format string')
    parser.add_argument('fval_regex', help='The regular expression to execute on the function\'s STDOUT stream with a capturing group representing the function value')
    parser.add_argument('-t', '--xtol', default=1e-6, type=float, help='Specify tolerance [default: %(default)s]')

    args, ini = parser.parse_known_args()

    if len(ini) < 1:
        parser.error("Incorrect number of arguments")

    cmd = command.format_fn(args.fn_call)
    val = value.regex_fn(re.compile(args.fval_regex))

    ext = optimization.external_fn(cmd, val)
    ini = [float(x) for x in ini]

    if args.direction == 'max':
        fmin = lambda x: -ext(x)
    else:
        fmin = ext

    ret = minimize(fmin, ini, method='nelder-mead', options={'xtol': args.xtol})

    print(ret)

