#!/usr/bin/env python
# coding: utf-8

# # Conditional execution 
# 
# ## If-else statements

# _If_ statements are used to execute a set of commands only under certain conditions. The syntax is shown below. Note that the commands to be run conditionally are indented with a tab.

# In[1]:


x = 1
if x > 0:
    print('x is positive')
    print('another line')
if not x > 0:
    print('x is negative')
print('done')


# A chain of conditions can be created with `if`, `elif` and `else` blocks.

# In[2]:


if x > 0:
    print('x is positive')
elif x < 0:
    print('x is negative')
else:
    print('x is zero')


# __Exercise:__
# 
# Using conditional execution, calculate the absolute value of a number (not using the built-in `abs` function).

# ## Exceptions
# 
# Conditional execution - same category as if statements. The code in the `try` statement is run first. If an error occurs while running that code, the code under the `except` statement is run instead.

# In[3]:


a = 'year'
b = 2022


# This gives an error, because strings cannot be combined with numbers. Execution of the program is stopped.

# In[4]:


a+b


# This tries the same code, and converts both variables to a string if an error occurs. Execution of the program continues.

# In[2]:


try:
    combined = a+b
except TypeError:
    combined = str(a)+str(b)
   
print(combined)

