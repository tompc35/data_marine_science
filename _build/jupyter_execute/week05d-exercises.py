#!/usr/bin/env python
# coding: utf-8

# # Exercises
# 
# ## Week 5

# ### Conditional execution
# a. Calculate the absolute value of a number (not using the built-in abs function). Use the following code as a template (replace the dashes ----- with code).
# 
# ```
# x = ------
# if -----:
#     absx = -----
# else:
#     absx = -----
# 
# print('the absolute value of x is',absx)
# ```

# b. Using conditional execution, determine whether a user-provided integer x is even or odd and print the result (hint: the % operator calculates the remainder that occurs when dividing two numbers, e.g. the result of    7 % 3 is equal to 1).
# 
# ```
# xin = input('Please enter a number:')
# x = int(xin)
# if ------:
#     --------
# else:
#     print(‘The number is odd’)
# ```
# 
# c. Modify the code written in part b to use try and except statements to handle non-integer input gracefully. If the input is not an integer, the program should print a friendly message explaining what went wrong. 
# 
# d. (if time) Modify the code written in part b above to continue requesting input until an integer is provided.
# 
# ### Grain size classification (if time)
# 
# Write a function that takes sediment grain size as an input, then returns the Wentworth grain size classification based on the table below.
# 
# |  Grain Size   | Classification   |
# | ------------- | ------- |
# | >= 256 mm     | Boulder |
# | 64-256 mm     | Cobble  |
# | 2-64 mm       | Gravel  |
# | 62.5 &mu;m - 2 mm| Sand    |
# | 3.9-62.5 &mu;m   | Silt    |
# | 0.98-3.9 &mu;m   | Clay    |
# 
# Test the program repeatedly to make sure it works for different input values.
# 
# ### Python modules
# 
# a. Write two more unit conversion functions (converting one way and back). 
# 
# b. Use one in the `if __name__ == '__main__':`  section of convert.py
# 
# c. Use the other in myscript.py
# 
# d. Run these files from the shell, and see what parts of the code are run 
#     
# e. Think about what other functions would be useful in your research (conversion or otherwise). If time, try to implement one or more of these functions in a module.

# In[ ]:




