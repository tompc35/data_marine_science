#!/usr/bin/env python
# coding: utf-8

# # Python packages
# 
# ## Importing a module located in a another directory - two options
# 
# Often, the module that you want to import is not in the current directory you are working in. For example, you may want to have a set of useful functions stored in a `MyTools` directory somewhere on your computer, and be able to access those functions from multiple different project directories.
# 
# ### Option 1: Setting your PATH
# 
# In order to import a module, Python has to know where to look for it. It knows to look in the current diectory (say, the directory from which you are running a script), but it does not search your entire computer.
# 
# You can specify  directories where Python should look for modules. 
# 
# * Add a directory (e.g. `path/to/MyTools`) to your PYTHONPATH with the following Python commands:
# 
# ```python
# import sys
# sys.path.append("path/to/MyTools")
# ```
# 
# A good way to keep track of things is to keep all of your useful modules in one directory on your computer, then add that single directory to your PATH. If you ever want to share your code with somebody else, it will help to not have files scattered all over your computer. See [this blog post by Brown Dwarf Research](http://www.bdnyc.org/2012/09/editing-pythonpath-to-import-modules/), where the above example came from, for more really useful information.
# 
# ### Option #2 (better): Creating a package
# 
# In the example above, if you edit your path using `sys.path`, the changes are not permanent. There are several ways of adding modules to you path permanently. The best option, which works on any operating system, is to create and install your own package. To create a package called `mytools`, the basic directory stucture should look like this:
# 
# ```
# MyTools/
#     setup.py
#     mytools/
#         __init__.py
#         convert.py
# ```
# 
# Here, `convert.py` is a Python file containing your useful functions in a module. The `__init__.py` file is empty (if you wish, it could be used to execute code upon importing the `mytools` package).
# 
# The `setup.py` file describes the contents of the package, and the location of module files. An example of the contents of a minimal `setup.py` file is shown below:
# 
# ```python
# from setuptools import setup
# 
# setup(name='mytools', 
#       packages=['mytools'])
# ```
# 
# A more complete `setup.py` file would include more information describing the package:
# 
# ```python
# from setuptools import setup
# 
# setup(name='mytools', 
#       packages=['mytools'],
#       version=0.1,
#       author='Tom Connolly',
#       author_email='tconnolly@mlml.calstate.edu',
#       description='A collection of useful Python tools.',
#       license='CC BY')
# ```
# 
# Once you have created the package, run this command in the shell (making sure the `MyTools` directory is your present working directory):
# 
# ```bash
# pip install -e .
# ```
# 
# You can also run this command from the Python console if you precede it with a `!`:
# ```python
# !pip install -e .
# ```
# 
# The `!` tells Python to run the command in an operating system shell, rather than executing it as Python code.
# 
# Here, `pip` is a package manager (included in Anaconda), the -e indicates that the package should be installed in "developer mode" (so you do not have to re-run pip if you make changes,), and `.` indicates the present working directory. Now your package is installed and your tools are on the Python path and available to imported whenever you start up Python.
# 
# ```python
# from mytools import convert
# 
# convert.f2c(32.0)
# ```
# 
# The package described above is very basic. You can add many more module files to the `mytools` directory, in addition to `convert.py`. You can also add additional directories, if you have categories of modules that you want to organize within the package. If you want to share your package, you can put it on Github or even put it on the Python package index, so that others can automatically `pip install` it. More useful information on packages can be found at https://python-packaging.readthedocs.io/en/latest/

# In[ ]:




