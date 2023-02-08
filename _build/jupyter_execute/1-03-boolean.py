#!/usr/bin/env python
# coding: utf-8

# # Boolean logic in Python
# 
# In the 19th century, in a book called _The Laws of Thought_, an Irish mathematician named George Boole developed a formal system of logic that laid the foundation for conveying information electronically. Boolean variables are a special type of variable that has two possible values: `True` or `False`. These binary values can also be represented as `1` or `0`. 

# In[1]:


a = True
type(a)


# In Python, a double equals sign (`==`) tests for equivalancy. This is much different from the single equals sign (`=`), which is used for assignment (assigning a value to a variable).

# In[2]:


print(1==1)
print(1==2)


# In[3]:


# 1 and 0 can also represent True or False
print(1==True)
print(1==False)


# In[4]:


# test for non-equivaalence
print(1 != 3)
print(1 >= 3) 


# In[5]:


print(0 == 1)


# In[6]:


print(0 == False)


# ### Exercise
# 
# Predict the output from each of the following three lines of code.
# 
# ```
# print(True == (0 == 3))
# ```
# 
# ```
# (False == (1 == True)) != False
# ```
# 
# ```
# False = False
# ```

# ## Logic gates
# 
# In electronics, logic gates take multiple binary values (on/off) as input and produce a single binary value as output. These logic gates follow the laws of Boolean algebra. The same types of logic gates are used in computer programing. One type of logic gate is the __AND__ gate. The AND gate produces a `True` value only if both inputs are `True`.
# 
# A logic gate performs a logical operation on multiple binary inputs, resulting in a single binary output.

# In[7]:


print(0 and 0)
print(0 and 1)
print(1 and 0)
print(1 and 1)


# The __OR__ gate produces a `True` value if at least one input is `True''.

# In[8]:


print(0 or 0)
print(0 or 1)
print(1 or 0)
print(1 or 1)


# Element-wise boolean logic with Numpy 
# * Use `&` for *and*
# * Use `|` for *or*

# In[9]:


import numpy as np
np.array([True,False,True]) | np.array([True,False,False])

