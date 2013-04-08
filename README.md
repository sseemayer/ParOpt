# Paropt - generic command-line parameter optimization

Paropt is a python tool for optimizing an application's parameters using system calls and parsing performance data from STDOUT. From a starting value, it will call the command line given to it repeatedly, converging into optimal parameters using the [Nelder-mead](http://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method) algorithm or grid search.

## Usage

     popt [options] {min,max} fn_call fval_regex x0 x1 x2 ...
     popt -g [options] {min,max} fn_call fval_regex x0range x1range x2range ...

### Positional Arguments

  * `{min,max}` The direction of optimization
  * `fn_call` A valid system call with placeholders (`{}` or numbered with `{0}`, `{1}`, etc.) representing parameters, e.g. `'examples/rosenbrock.py {} {}'`.
  * `fval_regex` A valid regular expression that contains a capturing group representing the function value to parse out, e.g. `'fx = (.*)'`

All additional positional arguments will represent initial values for the variables - make sure the number of variables matches your function call!

### Optional Arguments

  * `-g` `--grid` Use grid search (see *Range specifications* for details on how to specify value ranges)
  * `-n` `--neldermead` Use nelder-mead (default)
  * `-h` `--help` Display help
  * `-t` `--xtol` Specify a tolerance value for the optimization (default: 1e-6)
  * `-i` `--maxiter` Specify the maximum number of iterations for the optimization (default: None)

### Range specifications

If optimizing using grid search, variables are not given as initial values but as ranges specifying the grid search space. Ranges are specified as 1-, 2- or 3-tuples giving minimal and maximal values plus an optional increment. Examples:

	0,1,0.1	A range from 0 to 1 in increments of 0.1 (e.g 0.1, 0.2, ... 0.9)
	1,4	A range from 1 to 4 in increments of 1 (e.g. 1, 2, 3)
	0.5	A range from 0.5 to 0.5 (i.e. a constant value)

Valid delimiter characters are: `,;|`

## Example

### Nelder-mead optimization

The following example minimizes the Rosenbrock banana function located in `examples/rosenbrock.py` in 5 variables.

Let's say we have a python program calculating the value of the Rosenbrock function that takes values from the command line and returns the value of the function in STDOUT:

    $ examples/rosenbrock.py 1.3 0.7 0.8 1.9 1.2
    fx = 8.4822000000e+02 

We can minimize this function using popt:

    $ ./popt --xtol 1e-8 min 'examples/rosenbrock.py {} {} {} {} {}' 'fx = (.*)' 1.3 0.7 0.8 1.9 1.2
    [...]
    success: True
    status: 0
    nfev: 571
    fun: 4.8611534334e-17
    nit: 339
    message: 'Optimization terminated successfully.'
    x: array([ 1.,  1.,  1.,  1.,  1.])

### Grid search optimization

The following example minimizes the Rosenbrock banana function located in `examples/rosenbrock.py` in 2 variables using grid search covering the grid `[0, 0.1, ... 1.9]` for each of the variables.

	$ ./popt -g min 'examples/rosenbrock.py {} {}' 'fx = (.*)' 0,2,0.1, 0,2,0.1

## Dependencies

* Python 3.3 or better (I will probably make this more downward-compatible later, but for now I'm enjoying the cutting edge :D)
* scipy 0.12
