#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python
# 
# This tutorial introduces basic Python syntax, commands and variable types. We will be using the Anaconda distribution of Python (see installation instructions [here](software-installation)).
# 
# ## Ways of using Python
# 
# ### 1. Interactive mode
# 
# #### Using the Python interpreter
# 
# There are different ways of using Python. One way is to enter one command at a time in an "interactive" mode.
# 
# To start Python in interactive mode, execute `python` on the Terminal (Mac) or Anaconda Prompt (Windows).

# ```bash
# python
# ```

# This will start the Python interpreter, where commands can entered one at a time. The chevrons `>>>` indicate an interactive command prompt, which is waiting for your input.

# ```
# Python 3.7.2 (default, Dec 29 2018, 00:00:04)
# [Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>>
# ```

# ##### Hello, World
# Typically, the first program that people write when learning and new program is the "Hello, World!" program. This is a tradition that dates back to the 1970's, and it is useful for showing the basic syntax of a language.

# ```
# print('Hello, World!')
# ```

# To exit the the Python interpreter, type `quit()`.

# #### The IPython interpreter

# * Execute `ipython` on the Terminal (Mac) or Anaconda Prompt (Windows). Type the same `print('Hello, World!')` command at the interactive prompt. What differences do you notice?

# ### 2. Running a script file

# Python commands can also be saved in script files, which can be executed from the command line.
# 
# Using Atom, Nano or any other text editor, create a file called `my_script.py`. In the file type the same `print('Hello, World!')` command. Now run the script be entering the following on the Terminal (Mac) or Anaconda Prompt (Windows):

# ```bash
# python my_script.py
# ```
# 
# Just like shell scripts, Python scripts can contain a series of different commands, and you do not have to type them in one at a time. When a filename is specified, Python executes the commands in that file instead of opening an interactive prompt.

# ### 3. Notebooks 
# 
# Notebooks allow users to run code, display figures and type formatted text in one file. In this class, we will be using "Jupyter Notebooks," which can be run in the Julia, Python and R languages (as well as many others).
# 
# JupyterLab is an integrated development environment that provides an interface to navigate files, edit text files, run scripts and create notebooks. Start JupyterLab by typing on the Terminal (Mac) or Anaconda Prompt (Windows):

# ```bash
# jupyter lab
# ```

# This brings up a graphical user interface, which can be used to create a new notebook file.

# ## Syntax
# 
# These are the rules of the language. Think of it as grammar.

# `'Hello, World!'` is an example of a __string__, which is a set of characters. Strings are indicated by enclosing them in quotes. They can be single quotes ' ' or double quotes " ", but note a combination of the two.
# 
# `print()` is an example of a __function__. A function is a self-contained program that can take input and return output, or just execute a set of instructions. The `print()` function takes whatever input is given between the parentheses and prints it to the screen. The `print()` function is an example of a built-in function. It is part of the Python language. Later, we will write our own functions, a powerful tool in programming.
# 
# In addition to printing strings, the `print()` function can also print numerical values. If you do arithmetic inside the parentheses, those operations are executed first and the answer is printed to the screen.

# In[1]:


print('Hello MS263')
print(6)
print(4+6)


# If you get a `SyntaxError` it means Python can't handle something you've done because of incorrect syntax. In real life, we can sometimes break rules of syntax and get away with it. When communicating with computers in a language like Python, there is no room for error.
# 
# ##### Exercise
# 
# The following lines of code will raise a `SyntaxError`, can you see why?

# ```
# print('Hello, World!'
# 
# print('Hello, World!'))
# 
# print('Hello, World!")
# 
# print('Hello, World!)
# ```

# In[2]:


# this is a comment
# you can take notes
# in comment lines
# Python will ignore them


# ## Variables
# 
# A __variable__ is information that is stored and labeled with a symbolic name.

# In[3]:


a = 4
print(a)


# In the code above, `a` is the name of the variable and `4` is a value being stored in the variable. You can think of a variable as a container for information, and the name of the variable is label on the container. 
# 
# Python commands like `print()` use the value of the variable, or the information that is being stored in the container. In this case the value `4` is printed rather than the name of the variable `a`.
# 
# The equals sign = indicates __assignment__. It is used to assign a value to a variable. The variable name is always on the left side of the =, and the value is always on the right.
# 
# Variable names do not have to be just one letter. The can contain can contain multiple characters, numbers and underscores.

# In[4]:


var_1 = 8
print(var_1)


# 
# Python does not try to interpret anything within a string as instructions. However, unlike comments, strings are not just ignored. A string is treated as information in the form of text characters, which can be used or manipulated.
# 
# Characters not in quotes are interpreted as instructions, like `print()`, or variable names that are symbolic of underlying information, like `string_variable` in the code below.

# In[5]:


string_variable = 'abc'
print(string_variable)


# Variables cannot start with a number or contain special characters (except underscore \_). The following code would therefore raise an error.

# ```python
# 2& = 8 
# ```

# ##### Excercise
# 
# Without running any code, predict the output of the following three-line program.

# ```python
# a = 16 
# a = a+2  
# print(a)
# ```

# ### User input*
# 
# Another example of a function that takes input and produces output is `input()`. This function waits for the user to type something, and then stores that input in a variable. This puts the user input into a container that can be used later.

# ```python
# i = input('give me information') 
# ```

# This is just one type of user input. Data files are another example of user input that can be read and maniplulated. Later we will learn multiple ways of reading files.

# ### Variable types

# #### Integer 
# No decimal point. Exact.

# In[6]:


i = 4
print(i)
print(type(i))


# #### Floating point
# 
# Adding a decimal point creates a floating point number, which is stored on the computer in a completely different way and is only an approximation.  A floating point is what computer scientists call a number with a decimal point.  A floating point number is really an approximation of a number, compared to an integer which is an exact number.

# In[7]:


f = 4.0
print(f)
print(type(f))


# #### Complex numbers*

# In[8]:


c = 3 + 2j
print(c)
print(type(c))
print('real part',c.real)
print('imaginary part',c.imag)


# #### String

# In[9]:


s = 'hello'
print(s)
print(type(s))


# Strings can contain any type of charatcer, including numbers.  Quotes means it's a string that contains the number four.  It means we can do different operations with it as a string.

# In[10]:


s2 = '4'
print(s2)


# #### Converting between variable types
# 
# Built-in Python functions can be used to convert a variable to a different type. For example, `int()` can convert a string to an integer (if the string is a number...if the string is letter characters, python will give an error).

# In[11]:


s = '16'
si = int(s)
print(si)
type(si)


# An integer can be coverted to a floating point number. The value is the same, but it is stored on the computer in a different way (with bits devoted to the sign, exponent and mantissa).

# In[12]:


sf = float(si)
print(sf)
print(type(sf))


# ##### Excercise
# 
# What type of value is 3.4 + 5? How can you find out using Python?

# Adapted from:
# http://swcarpentry.github.io/python-novice-gapminder/03-types-conversion/index.html

# ##### Exercise
# 
# What type of value (integer, floating point number, or character string) would you use to represent each of the following? There may be more than one good answer for each problem.
# 
# 1. Current population of a city.
# 2. Average population of a city over time.
# 3. Serial number of a piece of lab equipment.
# 4. Time elapsed from the start of the year until now in days.
# 
# Adapted from:
# http://swcarpentry.github.io/python-novice-gapminder/03-types-conversion/index.html

# #### Combining integers and floats
# 
# Python easily allows integers and floats to be combined in mathematical calculations. The resulting number is a float. 

# In[13]:


a = 4.0
b = 2 
print(a+b)
print(type(a+b))


# #### Other mathematical calculations

# In[14]:


print(a-b)    # subtraction
print(a*b)    # multiplication
print(a**2)   # raise to power of 2
print(a**0.5) # square root
print(a/b)    # division


# #### Division in Python
# 
# The way Python divides two integers has actually changed between Python 2 and 3. Python 2 used to use floor division as the default method of dividing two integers.  Python 3 just creates a float from the two integers. The change in behavior of dividing two integers is one of the biggest differences between Python 2 and 3.
# 
# The old Python 2 behavior was a holdover from compiled laguages like C, where types are __static__ and have to be explicitly defined. In this case, results of an operation involving two integers is another integer. In Python, types are __dynamic__ and do not have to be explicitly defined. Instead, the are implied, by adding a decimal point to a number (float) or surrounding with quotes (string).

# In[15]:


print(2/3)    # dividing two integers in Python 3 
print(2//3)   # floor division


# #### Order of operations
# 
# The order in which mathematical operations are done follow the usual rules, including doing operations enclosed in parentheses first.

# In[16]:


print( 3*(4+6) )


# #### An example of round-off error
# 
# For more information on errors in floating point arithmetic see:
# https://docs.python.org/3/tutorial/floatingpoint.html

# In[17]:


print(3.0/10.0)
print(3*0.1)


# #### Concatenating strings
# 
# The plus sign (+) does not just have one meaning. It can also be used to add one string to the end of anoather.

# In[18]:


a = 'Py'
b = 'thon'
print(a+b)


# ##### Exercise
# 
# The following variables are assigned in Python:
# 
# ```python
# first = 1.0
# second = "1"
# third = "1.1"
# ```
# 
# Which of the following will return the floating point number 2.0? Note: there may be more than one right answer.
# 
# 1. `first + float(second)`
# 2. `float(second) + float(third)`
# 3. `first + int(third)`
# 4. `first + int(float(third))`
# 5. `int(first) + int(float(third))`
# 6. `2.0 * second`
# 

# ```{toggle}
# 1. Correct
# 2. Gives incorrect answer of 2.1
# 3. Gives a value error because "1.1" cannot be converted to an integer
# 4. Correct
# 5. Gives the integer value 2, not a floating point
# 6. Gives a type error because a string cannot be multiplied by a float
# ```

# ### Lists
# 
# * In many situations, we do want to store just one data value, we want to store a collection of data values. One way to do this is with a list. Square brackets denote this as a list.

# In[19]:


t = [5,3.9,4.2]
print(type(t))


# * Lists can inlude both numbers and strings. Each element of a list has an index. Indices start at 0.
# * Indices can also be accessed from the back.  To call the last element, use [-1].  In this example, the last element can be accessed forwards with [2] or backwards [-1].

# In[20]:


t = [5,3.9,'a string']
print(t)
print(t[1])
print(t[2])
print(t[-1])


# * Indexing can be used to assign new values within lists.

# In[21]:


t[1] = 'new item'
print(t)


# * Lists can also be nested within lists.

# In[22]:


t2 = [5,3.9,[1,2,3]]
print(t2)
print(t2[2])
print(t2[2][1])


# * Strings have indexing as well.  If you type s3[1:3] python will start at index 1, and include it and everything up to, but not including, index 3.
# 
# 

# In[23]:


s3 = 'hello'
print(s3[1])
print(s3[1:])
print(s3[:1])
print(s3[1:3])
print(s3[-3:-1])


# * Some other basic built-in functions for lists. '__len__' is short for length, and a function that can be used for lots of different variable types.  It returns the number of items in the list.

# In[24]:


t = [0,2,3]
print(len(t)) # length
print(sum(t)) # sum
help(len)


# ##### Exercise
# 
# Use slicing to access only the last four characters of a string or entries of a list. The following variables have been created in Python:

# In[25]:


string_for_slicing = "Observation date: 02-Feb-2013"
list_for_slicing = [["fluorine", "F"],
                    ["chlorine", "Cl"],
                    ["bromine", "Br"],
                    ["iodine", "I"],
                    ["astatine", "At"]]


# What Python code creates the following output? Would your solution work regardless of whether you knew beforehand the length of the string or list (e.g. if you wanted to apply the solution to a set of lists of different lengths)? If not, try to change your approach to make it more robust.
# 
# ```
# "2013"
# 
# [["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
# ```
# 
# Adapted from:
# http://swcarpentry.github.io/python-novice-inflammation/05-lists/index.html

# In[26]:


string_for_slicing[25:]


# In[27]:


list_for_slicing[1:5]


# ### Tuples
# 
# Tuples are immutable

# In[28]:


my_tuple = (1,2,3)
type(my_tuple)


# This code gives an error because you cannot change a tuple after it has been created.
# 
# ```python
# my_tuple[1] = 5
# ```
# 
# Why use a tuple? In certain situations, using a tuple is much more efficient than using a list. The main reason we are introducing it here is that some functions provide output in tuples, so it is good to know what they are.

# ### Dictionaries
# 
# Dictionaries are like lists but use keys instead of numerical indexing.

# In[29]:


my_town = {'name':'Moss Landing','state':'California'}


# In[30]:


my_town['name']


# In[31]:


my_town['zip'] = 95039


# In[32]:


my_town


# ##### Exercise
# 
# Modify the `my_town` dictionary to include a list of restaurants in Moss Landing.

# In[33]:


my_town['restaurants'] = ['Whole Enchilada','Haute Enchilada','Phil\'s']


# ## Numpy
# 
# NumPy (Numerical Python) is a __package__ that extends Python's basic capabilities and allows for more complex mathematical operations involving groups of numbers. Importing the numpy __module__ gives access to its functions.

# In[34]:


import numpy as np


# We will use this package extensively, and this line of code will be at the top of nearly every program we write in this class. We give the numpy module a "nickname," or __alias__, so it is quicker to type. Giving numpy the alias `np` is standard practice.
# 
# The numpy library gives access to special mathematical functions, like square root.

# In[35]:


val = 2
val_sr = np.sqrt(2)
print(val_sr)


# A list of mathematical functions available in NumPy can be found on the [SciPy documentation website](https://docs.scipy.org/doc/numpy/reference/routines.math.html).
# 
# NumPy also gives access to a new variable type: the NumPy array. Arrays are similar to lists, but they contain only numbers. We will use NumPy arrays to store numeric data throughout this course. 
# 
# A list of numbers can be converted to an array.

# In[36]:


num_list = [1,2,3]
num_arr = np.array(num_list)
print(num_arr)
print(type(num_arr))


# Arrays behave differently from lists. Multiplication and addition operatations _replicate_ lists, but these operations act on each individual _elements_ in an array.

# In[37]:


print(num_list*2)


# In[38]:


print(num_arr*2)


# We will learn more about arrays throughout the semester.

# ##### Exercise

# Consider the following array of numbers:
# 
# `my_array = np.array([5.,7001.,-100,3.4,85.0004])`
# 
# Write your own Python code to calculate the mean of `my_array`. Make sure your code still works if the contents of `my_array` are changed to have different values, or a different number of values.
# 
# Check the results of your code with the results of the built-in Numpy function, `np.mean`:
# 
# `np.mean(my_array)`
# 

# ##### Exercise
# 
# Write your own Python code to calculate the standard deviation of `my_array`. Make sure your code still works if the contents of `my_array` are changed to have different values, or a different number of values.
# 
# Check the results of your code with the results of the built-in Numpy function, `np.std`:
# 
# `np.std(my_array)`

# Tips
# * use variables instead of repeating the same commands
# * use descriptive variable names, i.e. `N=len(values)`
# * use `help()`
