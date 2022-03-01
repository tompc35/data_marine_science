#!/usr/bin/env python
# coding: utf-8

# # Creating your own Python module
# 
# Up to this point, we have created functions and used them within the same Python script. However, what if we want to use those functions in another file, or another project entirely? To do this you can create your own module that can be imported in another Python scripts.
# 
# ## Running a file as a script from the shell command line
# 
# To show how modules work in Python, we start with a simple unit conversion module contained in the file [convert.py](scripts/convert.py):
# 
# ```python
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 
# '''A module for converting units.'''
# 
# def temp_f2c(f):
# 	''' This function converts Fahrenheit to Celcius
# 	Input: temperature in degrees F
# 	Output: temperature in degrees C
# 	'''
# 	c = (f - 32.0)*(5.0/9.0)
# 	return(c)
# 	
# def temp_c2f(c):
# 	''' This function converts Celcius to Fahrenheit
# 	Input: temperature in degrees C
# 	Output: temperature in degrees F
# 	'''
# 	f = c*(9/5) + 32
# 	return(f)
# 	
# if __name__ == '__main__':
# 	print('do this stuff if run as script')
# 	print('32 degrees F:',temp_f2c(32),'C')
# ```

# ### Breaking down parts of the file
# 
# This Python file has several parts. The first two lines are comment lines, and are therefore not run as Python code. However, they contain important information about the file and they are include automatically when you create a new file in Spyder. The first line,
# 
# ```python
# #!/usr/bin/env python3
# ```
# 
# is the "shebang" line, and this is specific to Unix-based operating systems (like Mac OSX and Linux). It tells the shell that this file can be run as a scipt. The second line,
# 
# ```python
# # -*- coding: utf-8 -*-
# ```
# 
# specifies how the text file that contains the source code is formatted. This line allows you to use Unicode characters. Both of these lines are optional. The next line,
# 
# ```python
# '''A module for converting units.'''
# ```
# 
# is a docstring for the module, which helps a user figure out what is in the module and what its purpose is. Like the comment lines, this line is not run as code. After the doc-string, two function are defined, and then comes another part of the file.
# 
# ```python
# if __name__ == '__main__':
# 	print('do this stuff if run as script')
# 	print('32 degrees F:',temp_f2c(32),'C')
# ```
# ### Running the file
# 
# The part of the file above is only run as a script (not when it is imported as a module in another Python file, which is what will be demonstrated in the next section). In Spyder, this can be done with the "Run" button. Python scripts can also be run from the shell (e.g. Mac Terminal, or Git Bash shell). The convert.py file can be run by navigating to its directory in the shell and typing
# 
# ```
# python convert.py
# ```
# 
# which gives the following output:
# 
# ```
# do this stuff if run as script                                                                              
# 32 degrees F: 0.0 C       
# ```
# 
# Running a python file in this way executes all of the Python code in the file, including the contents of the section that starts with `if __name__ == '__main__':`
# 
# ## Importing as a module
# 
# To show how to import the convert.py as a module, and use the functions in another file, we create a simple script called [myscript.py](scripts/myscript.py):
# 
# ```python
# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# 
# import convert
# 
# ctemp = 40
# ftemp = convert.temp_c2f(ctemp)
# print(ctemp,'C is ',ftemp,'F')
# ```
# 
# ### The import statement
# 
# In the file above, the conversion module is imported with the statement:
# 
# ```python
# import convert
# ```
# The functions in that module can then be used, like in the line:
# 
# ```python
# ftemp = convert.temp_c2f(ftemp)
# ```
# 
# ### Running the file
# 
# This file can be run from the shell, with the command,
# 
# ```
# python myscript.py
# ```
# 
# which gives the following output:
# 
# ```
# 40 C is  104.0 F   
# ```
# 
# It is also important to note what is code is _not_ run, which is the contents of the `if __name__ == '__main__':` section of convert.py. When a Python file is imported as a module, this part of the code is not run. This is a good place to put demonstrations of functions in a module, or tests.
# 
# ## Exercises
# 
# * Write two more unit conversion functions (converting one way and back).
# * Use one in the `if __name__ == '__main__':` section of convert.py
# * Use the other in myscript.py
# * Run these files from the shell, and see what parts of the code are run

# In[ ]:




