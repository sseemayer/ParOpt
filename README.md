# Paropt - generic command-line parameter optimization

Paropt is a python toolkit for optimizing an application's parameters using system calls and parsing performance data from STDOUT. From a starting value, it will call the command line given to it repeatedly, converging into optimal parameters using the [Nelder-mead](http://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) algorithm.

## Example

The following example optimizes the Rosenbrock banana function located in `examples/rosenbrock.py` in 5 variables using popt:

    $ ./popt --xtol 1e-8 'examples/rosenbrock.py {} {} {} {} {}' 'fx = (.*)' 1.3 0.7 0.8 1.9 1.2
    [...]
    success: True
    status: 0
    nfev: 571
    fun: 4.8611534334e-17
    nit: 339
    message: 'Optimization terminated successfully.'
    x: array([ 1.,  1.,  1.,  1.,  1.])

## Dependencies

* Python 3.3 or better (I will probably make this more downward-compatible later, but for now I'm enjoying the cutting edge :D)
* scipy 0.12
