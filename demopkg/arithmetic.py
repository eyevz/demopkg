"""
This is module-level documentation that will be used by documentation tools when creating API docs.
"""

import numpy as np

def add_numbers(*args, **kw):
  """Returns the sum of input numbers.
  Sequential arguments are collected into an array and passed as the first argument to numpy.sum.
  Keyword arguments are collected and passed through to numpy.sum as keyword arguments.
  
  This text is called a docstring, and is accessible via add_numbers.__doc__. It will be used by
  documentation generation tools like Sphinx to create API documentation for your package. You
  can use reStructuredText for formatting and linking to other docs and websites.
  
  The text at the end of this docstring is called a doctest. For simple functions, doctests are
  quite useful during development and they also serve as examples of use.
  
  The doctests can be run from the command line as follows::
  
    python -m doctest [-v] arithmetic.py
  
  The optional switch -v turns on verbose mode, generating output even if there are no test
  failures.
  
  >>> add_numbers(1,2)
  3
  >>> add_numbers(1,2,3,4)
  10
  >>> x = range(4)
  >>> add_numbers(*x)
  6
  """
  return np.sum(args, **kw)
