#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# Functions can be used to package a set of instructions. These instructions can then be reused for different inputs. Using functions can save you a lot of copying and pasting. Also, if you find a bug in your set of instructions, you only have to fix it once if you use a function instead of copying and pasting.

# In[1]:


def fahr_to_celsius(temp_fahr):
    ''' Convert temperature from degrees F to C '''
    temp_celsius = (temp_fahr - 32) * (5/9)
    return temp_celsius


# In[2]:


help(fahr_to_celsius)


# In IPython (and Jupyter notebooks) there is another way of asking for help by typing the function name with a question mark.
# 
# `mean?`
# 

# To use the function:

# In[3]:


fahr_to_celsius(32)


# In[4]:


tempF = 212

tempC = fahr_to_celsius(tempF)
print('Temperature in Celsius is:',tempC)


# #### Multiple outputs

# In[5]:


def fahr_to_celsius_kelvin(temp_fahr):
    ''' Convert temperature from degrees F to Celsius and Kelvin '''
    temp_celsius = (temp_fahr - 32) * (5/9)
    temp_kelvin = temp_celsius + 273
    return temp_celsius,temp_kelvin


# In[6]:


fahr_to_celsius_kelvin(77)


# #### Specifying default values for inputs

# In[7]:


def fahr_to_celsius_kelvin(temp_fahr=32):
    ''' Convert temperature from degrees F to Celsius and Kelvin '''
    temp_celsius = (temp_fahr - 32) * (5/9)
    temp_kelvin = temp_celsius + 273
    return temp_celsius,temp_kelvin


# In[8]:


fahr_to_celsius_kelvin()


# __Exercises:__
#     
# * Create a function that takes a number as input, and returns the square of that number.
# * Create a function to calculate the standard deviation of an array (not using the `np.sqrt` function).
