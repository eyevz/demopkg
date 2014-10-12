from os import path
from setuptools import setup

import bdist_wheel

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'VERSION.txt')) as f:
  version = f.read().strip()

description = 'Package skeleton to demonstrate concepts for TCMTools.'

# REQUIREMENTS
# List just the requirements for a production installation. Additional requirements and tools for
# development are listed in dev-tools.txt.
install_requires=['numpy==1.9.0', 'scipy==0.14.0', 'pyzmq==14.3.1']

setup(
  name='demopkg',
  description=description,
  long_description=description,
  version=version,
  url='https://github.com/ivesn/demopkg',
  author='Norman Ives',
  author_email='norman.ives@gmail.com',
  license='Copyright Norman Ives 2014. All rights reserved.', 
  packages=['demopkg'],
  install_requires=install_requires,
  cmdclass={'bdist_wheel': bdist_wheel.bdist_wheel}
)
