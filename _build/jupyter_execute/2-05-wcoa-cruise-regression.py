#!/usr/bin/env python
# coding: utf-8

# # Implementing linear regression in Python
# 
# ## Example: 2007 West Coast Ocean Acidification Cruise 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats
import statsmodels.formula.api as smf
import pingouin as pg

import PyCO2SYS as pyco2


# ## Load data
# 
# ##### Load 2007 data

# In[2]:


filename07 = 'wcoa_cruise_2007/32WC20070511.exc.csv'
df07 = pd.read_csv(filename07,header=29,na_values=-999,parse_dates=[[6,7]])


# In[3]:


df07.keys()


# ### Linear regression: four methods in Python

# Create $x$ and $y$ variables.

# In[4]:


x = df07['PHSPHT']
y = df07['NITRAT']


# Plot data.

# In[5]:


plt.figure()
plt.plot(x,y,'.')
plt.xlabel('phosphate')
plt.ylabel('nitrate')


# Create a subset where both variables have finite values.

# In[6]:


ii = np.isfinite(x+y)


# In[7]:


ii


# #### Method 1: Scipy

# In[9]:


result = stats.linregress(x[ii],y[ii])


# In[10]:


result


# In[11]:


result.slope


# Exercise: Draw the regression line with the data

# In[12]:


plt.figure()
plt.plot(x,y,'k.')
plt.plot(x,result.slope*x+result.intercept,'r-')


# #### Method 2: statsmodels

# Ordinary least squares fit using [statsmodels](https://www.statsmodels.org/).

# In[16]:


smres = smf.ols('NITRAT ~ PHSPHT',df07).fit()


# In[17]:


smres.summary()


# #### Method 3: pingouin

# In[18]:


pg.linear_regression(x[ii],y[ii])

