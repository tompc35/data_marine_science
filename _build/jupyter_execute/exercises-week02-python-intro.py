#!/usr/bin/env python
# coding: utf-8

# # Exercises - Introduction to Python
# 
# ### Variable assignment
# 
# Without running any code, predict the output of the following three-line program.
# 
# ```
# a = 16 
# a = a+2  
# print(a) 
# ```
#  
# ### Types of numbers
#  
# What type of value is 3.4 + 5? How can you find out using Python?
# 
# ### Type overview
# 
# What type of value (integer, floating point number, or character string) would you use to represent each of the following? There may be more than one good answer for each problem.
# 
#  a. Current population of a city.
# 
#  b. Average population of a city over time.
# 
#  c. Serial number of a piece of lab equipment.
# 
#  d. Time elapsed from the start of the year until now in days.
#  
# 
# ### Appending variables
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
#  a. `first + float(second)`
# 
#  b. `float(second) + float(third)`
# 
#  c. `first + int(third)`
# 
#  d. `first + int(float(third))`
# 
#  e. `int(first) + int(float(third))`
# 
#  f. `2.0 * second`
# 
# ### Slicing
# 
# Use slicing to access only the last four characters of a string or entries of a list. The following variables have been created in Python:
# 
# ```python
# string_for_slicing = "Observation date: 02-Feb-2013"
# list_for_slicing = [["fluorine", "F"],
#                     ["chlorine", "Cl"],
#                     ["bromine", "Br"],
#                     ["iodine", "I"],
#                     ["astatine", "At"]]
# ```
# 
# What Python code creates the following output? Would your solution work regardless of whether you knew beforehand the length of the string or list (e.g. if you wanted to apply the solution to a set of lists of different lengths)? If not, try to change your approach to make it more robust.
# 
# ```
# "2013"
# [["chlorine", "Cl"], ["bromine", "Br"], ["iodine", "I"], ["astatine", "At"]]
# ```
# 
# ### Dictionaries
# 
# Add a new element to the `my_town` dictionary by creating a new key-value pair. The key should be `'restaurants'` and the value should be a list of names of eating establishments.
# 
# ### Numpy arrays
# 
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
# ### Standard deviation calculation
# 
# Write your own Python code to calculate the standard deviation of `my_array`. Make sure your code still works if the contents of `my_array` are changed to have different values, or a different number of values.
# 
# Check the results of your code with the results of the built-in Numpy function, `np.std`:
# 
# `np.std(my_array, ddof=1)`
# 
# Here, the `ddof` option refers to *delta degrees of freedom*. Using `ddof = 1` computes the unbiased standard deviation by using $N-1$ as the degrees of freedom instead of the default $N$.

# In[ ]:




