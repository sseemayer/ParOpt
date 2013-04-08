"""Minimization using Nelder-Mead (Downhill Simplex) Method"""

from scipy.optimize import minimize

def minimize_neldermead(fn, initial, xtol, maxiter):
    """Minimize a function using the nelder-mead algorithm"""

    ret = minimize(fn, initial, method='nelder-mead', options={'xtol': xtol, 'maxiter': maxiter})

    ret['message'] = 'Terminated successfully' if ret['success'] else 'Aborted'
    ret['variables'] = " ".join( '{:g}'.format(x) for x in ret['x'].tolist() )

    print("{message} after {nit} iterations and {nfev} function evaluations.\nThe optimal function value is {fun:g}\nOptimal variables:\n{variables}".format(**ret))
