import paropt.optimization
import paropt.command
import paropt.value
import re
from scipy.optimize import minimize

import optparse

def main():

    parser = optparse.OptionParser('Usage: %prog [options] "optimization_call {0} {1} {2}..." "regex_with (group)" x0 x1 x2 ...')
    parser.add_option('-t', '--xtol', dest='xtol', type='float', default=1e-6, metavar='XTOL', help='Specify tolerance [default: %default]')

    opt, args = parser.parse_args()

    if len(args) < 3:
        parser.error("Incorrect number of arguments")

    cmd, reg = args[0:2]
    ini = args[2:]

    cmd = command.format_fn(cmd)
    val = value.regex_fn(re.compile(reg))

    ext = optimization.external_fn(cmd, val)
    ini = [float(x) for x in ini]

    ret = minimize(ext, ini, method='nelder-mead', options={'xtol': opt.xtol})

    print(ret)

