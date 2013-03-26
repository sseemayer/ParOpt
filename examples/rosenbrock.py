#!/usr/bin/env python

import sys
import numpy as np

def rosenbrock(x):
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

if __name__ == '__main__':
    x = [ float(x) for x in sys.argv[1:]]
    val = rosenbrock(np.array(x))
    print("fx = {:.10e}".format(val))

