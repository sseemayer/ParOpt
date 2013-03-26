# Paropt - generic command-line parameter optimization

Paropt is a python toolkit for optimizing an application's parameters using system calls and parsing performance data from STDOUT. From a starting value, it will call the command line given to it repeatedly, converging into optimal parameters using the [Nelder-mead](http://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) algorithm.

## Usage

     popt [options] "optimization_call {0} {1} {2}..." "regex_with (group)" x0 x1 x2 ...

  * `optimization_call` is a valid system call using placeholders (`{}` or numbered with `{0}`, `{1}`, etc.) for parameters.
  * `regex` is a valid regular expression that contains a capturing group representing the function value to parse out
  * All additional positional arguments will represent initial values for the variables

### Options

  * `--t` `--xtol` Specify a tolerance value for the optimization (default: 1e-6)

## Example

The following example optimizes the Rosenbrock banana function located in `examples/rosenbrock.py` in 5 variables.

Let's say we have a python program calculating the value of the Rosenbrock function that takes values from the command line and returns the value of the function in STDOUT:

    $ examples/rosenbrock.py 1.3 0.7 0.8 1.9 1.2
    fx = 8.4822000000e+02 

We can optimize this function using popt:

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
