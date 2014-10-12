demopkg README
==============
This package is intended to demonstrate the basic package layout suitable for easy development and
distribution.

Installation for development
----------------------------
Installation into a Python environment for development is achieved by running::

  pip install -r dev-tools.txt -e .

from inside the directory containing the package, i.e., the directory containing setup.py.

The package will be installed into the environment via a reference to the source files in this
directory (this is the effect of the -e switch). As a result, changes to the package will be
visible to client code running in the environment without repeating the installation step.

The -r switch indicates additional packages to install.

It is recommended that a distinct virtual environment be used for development.

The command above will attempt to install the requirements from the normal Python package index.
This may be undesirable, and will typically require proxy configuration. Additional command line
options are available to instruct pip to search a particular location instead for distributions.

Running tests
-------------

nosetests --config=nose.cfg

Building for distribution
-------------------------

Simply run::

  python setup.py bdist_wheel

Appropriate defaults are set in setup.cfg.

Generating the documentation
----------------------------

In the docs directory, run::

  make html

See the `Sphinx documentation <http://sphinx-doc.org/>`_ for details.
