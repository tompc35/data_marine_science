#!/usr/bin/env python
# coding: utf-8

# # Loops

# Loops are a way of repeating commands over and over again.
# 
# A _while_ loop is an indefinite loop. It runs indefinitely until a certain condition is met. Be careful with while loops. If the condition is never met, the while loop will try to run forever.

# In[1]:


import numpy as np
i = 0
while i<5:
    i = i + 1
    print(i)
print('done with while loop')


# A _for_ loop is a definite loop. It iterates over a list, array or other variable types that are groups of values or other variables. It definitely stops when it gets to the end of the list.

# In[2]:


name_list = ['Bob','Jane','Mary']
for name in name_list:
    print("Hello " + name)
print('done')         


# An example of looping through a sequence of numbers created with the `np.arange()` function.

# In[3]:


import numpy as np
print(np.arange(5))


# In[4]:


print(np.arange(2,5))


# In[5]:


print(np.arange(2,5,0.5))


# In[6]:


for i in np.arange(5):
    print(i*2)


# __Exercise__:
# 
# Write a for loop that prints out the cumulative sum of an array. 
# 
# For example, the cumulative sum of the array
# 
# ```
# [1,3,6,4,7]
# ```
# 
# would be:
# 
# ```
# [1,4,10,14,21]
# ```
# 
# Write out your algorithm first. An algorithm is a process or set of rules followed in calculations or problem solving. It helps to write or sketch these instructions first, then translate the instructions to Python. This strategy helps break a coding problem up into smaller, more manageable parts.
# 
# Use the following code as a template (replace the dashes ----- with code).
# 
# ```python
# x = [1,3,6,4,7]
# 
# cumsum = 0
# for val in x:
#     cumsum = -------
#     print(cumsum)
# ```

# This should produce the output:

# In[7]:


x = [1,3,6,4,7]
cumsum = 0
for val in x:
    cumsum = cumsum + val
    print(cumsum)
print('done')


# ### For loop - cumulative sum 2
# 
# Write a for loop that stores the cumulative sum of an array in another array. Use the `np.append()` function - see `help(np.append)` - and make sure that you have run `import numpy as np`  at the top of your program in order to use this function.
# 
# ```python
# x = [1,3,6,4,7]
# 
# cumsum = 0
# cumsum_array = []
# for val in x:
#     cumsum = -------
#     cumsum_array = np.append(------,--------)
# 
# print(cumsum_array)
# ```

# This should produce the output:

# In[8]:


x_a = [1,3,6,4,7]
cumsum_a = 0
cumsum_array = []
for val in x_a:
    cumsum_a = cumsum_a + val
    cumsum_array = np.append(cumsum_array,cumsum_a)
    
print(cumsum_array)


# ### Fibonacci sequence (if time)
# 
# Write a for loop that prints the first n numbers of the Fibonacci sequence:
# 1,1,2,3,5,8,13…
# Write out your algorithm first, and start with the following minimal code. 
# 
# ```python
# n = 10
# 
# # insert code here
# ```
