"""Minimization using grid search"""

import itertools
import numpy

def minimize_grid(fn, vardef):
    """Minimize a function using grid search"""

    fmin = float('Inf')
    xmin = None
    neval = 0
    for varset in itertools.product(*vardef):
        neval += 1

        fval = fn(varset)

        if fval < fmin:
            fmin = fval
            xmin = varset

    print("Finished optimization after {} evaluations.\nThe optimal function value is {:.30f}\nOptimal variables: {}".format(neval, fmin, " ".join(["{:.3g}".format(x) for x in xmin])))
