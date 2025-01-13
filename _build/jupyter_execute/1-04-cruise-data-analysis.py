#!/usr/bin/env python
# coding: utf-8

# # Cruise data analysis in Python
# 
# ## WCOA 2013 data set
# 
# To download the data used in this tutorial, use the following command in the Terminal (Mac) or Git Bash (Windows).
# 
# ```
# git clone https://github.com/mlmldata24/wcoa_cruise.git
# ```
# 
# The data comes from the West Coast Ocean Acidification (WCOA) cruise in 2013. The goal of this NOAA-supported research cruise is to collect data to help understand the effects of coastal upwelling on ocean acidification, and the impacts of ocean acidification on organisms and ecosystems. [This video](https://www.youtube.com/watch?v=Eesi6e03Yx0&t=134s) gives an idea of life aboard the ship and the type of science operations conducted.
# 
# In this part of the tutorial, we will go over the basics of working with dates in Pandas and Numpy, make some exploratory plots and start a regression analysis. The data exploration will be largely guided by student interest.

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats


# ### Introduction to Pandas dataframes

# We use Pandas to import the csv data file. 
# 
# Here, there is an optional `parse_dates` argument. The numbers in double brackets `[[8,9]]` indicate which columns to interpret as dates.

# In[2]:


filename = 'data/wcoa_cruise/WCOA2013_hy1.csv'
df = pd.read_csv(filename,header=31,na_values=-999,
                 parse_dates=[[8,9]])


# In[3]:


df.head()


# In[4]:


df.columns


# Instead of strings, the dates are now in a special `datetime64` format. This means that, instead of treating the dates in the same way as any other collection of characters, pandas and NumPy can understand how this variable represents time.

# In[5]:


df['DATE_TIME'].head()


# For example, subtracting `datetime64` objects with pandas gives a `Timedelta` object, which is specifically used to represent differences between times. The first two samples in the cruise data are separated by 33 seconds (the time between firing of bottles).

# In[6]:


df['DATE_TIME'][1]-df['DATE_TIME'][0]


# In[7]:


pd.unique(df['LATITUDE'])


# #### Exercise
# 
# Create a list of unique station ID’s (“STNNBR”) found in the survey data. Call it `stns`. How many unique stations are there in the data? 
# 
# 
# 

# ### Summary statistics

# A summary of the dataframe is given by the `.describe()` method.

# In[8]:


df['CTDTMP'].describe()


# These summary statistics can also be accessed individually with similar syntax.

# In[9]:


df['CTDTMP'].mean()


# In[10]:


df['CTDTMP'].min()


# Alternate method using Numpy functions.

# In[11]:


np.min(df['CTDTMP'])


# ### Mathematical operations

# Converting Celcius to Fahrenheit

# In[12]:


df['CTDTMP_F'] = 9/5*df['CTDTMP'] + 32 


# In[13]:


df['CTDTMP_F'].head()


# In[14]:


df['CTDTMP'].head()


# ### Plotting

# Plot latitude as a function of time.

# In[15]:


plt.figure()
plt.plot(df['DATE_TIME'],df['LATITUDE'],'-o')
plt.xticks(rotation=15)


# The `pyplot` library automatically understands `datetime64` objects so it is easy to see how the ship moved between stations from north to south as weeks passed.

# In[16]:


plt.figure()
plt.plot(df['LONGITUDE'], df['LATITUDE'], 'ro')


# The `scatter()` function allows points to be colored according to the value of a variable. In the case of dates, later dates are shown as warmer colors.

# In[17]:


plt.figure()
plt.scatter(df['LONGITUDE'],df['LATITUDE'],c=df['DATE_TIME'])


# Note that the vertical coordinate is pressure (not depth, which indicates the bottom depth rather than the depth of the sample). To plot dissolved oxygen with depth:

# In[18]:


plt.figure()
plt.plot(df['OXYGEN'],df['CTDPRS'],'.')
plt.gca().invert_yaxis()

plt.xlabel('$O_2 [\mu M]$')
plt.ylabel('pressure[dbar]')


# In[19]:


plt.figure()
df['CTDTMP'].hist()


# In[20]:


plt.figure()
df['CTDTMP'].hist(bins=50)


# In[21]:


df.keys()


# #### Exercises
# 
# * What scientific questions can be addressed with this data set?
# * What relationships might occur between different variables?
# * What differences might occur within the same variables, but at different locations or times?
# * Create exploratory plots (one PDF, one scatter plot)

# ## Slicing and subsetting data

# In[22]:


df[0:3]


# In[23]:


df.iloc[0:3]


# In[24]:


df.loc[0:3]


# In[25]:


df.loc[0:3,['CTDTMP','CTDPRS']]


# #### Exercise
# 
# What do you expect to happen when you execute:
# ```
# df[0:1]
# df[:4]
# df[:-1]
# ```
# 
# What do you expect to happen when you call:
# ```
# df.iloc[0:4, 1:4]
# df.loc[0:4, 1:4]
# ```
# 
# How are the two commands different?
# 
# Adapted from: https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html

# ### Subsetting Data using Criteria

# In[26]:


df[df.LATITUDE > 40].head()


# In[27]:


df[df.LATITUDE <= 40].head()


# In[28]:


dfsub = df[(df.CTDPRS <= 10) & (df.LATITUDE > 40)]


# In[29]:


dfsub.head()


# ### Exercises
# 
# * Select a subset of rows in the `df` DataFrame that contains data from a pressure range between 500 and 1000 dbar. How many rows did you end up with? What did your neighbor get?
# 
# * You can use the isin command in Python to query a DataFrame based upon a list of values as follows:
# ```
# df[df['STNNBR'].isin([listGoesHere])]
# ```
# Use the `isin` function to find all samples from station numbers 11 and 12.

# ### Exercises
# 
# pH values are contained in the `df['PH_TOT']` DataArray
# 
# Quality control flags for pH are contained in the `df['PH_TOT_FLAG_W']` DataArray.
# 
# World Ocean Circulation Experiment (WOCE) quality control flags are used: 
# * 2 = good value
# * 3 = questionable value
# * 4 = bad value 
# * 5 = value not reported
# * 6 = mean of replicate measurements
# * 9 = sample not drawn.
# 
# 
# 1. 1. Create a new DataFrame called `dfsub1` that includes only data where pressure is less than 10 dbar and the latitude is farher north than $40^{\circ} \text{N}$.

# In[30]:


dfsub = df[(df['CTDPRS'] > 10) & (df['LATITUDE'] > 40)]


# 2. Create a new DataFrame called `dfsub2` that excludes all bad, questionable and missing pH and CTD oxygen values. Plot oxygen vs. pH.

# In[31]:


dfsub2 = df[(df['CTDOXY_FLAG_W'] == 2) & (df['PH_TOT_FLAG_W'] == 2)]


# ### Fit a linear model in Python

# In[32]:


plt.plot(df['CTDOXY'],df['PH_TOT'],'.')
plt.xlabel('dissolved oxygen [$\mu$mol/kg]')
plt.ylabel('pH$_{Tot}$')


# In[33]:


result = stats.linregress(dfsub2['CTDOXY'],dfsub2['PH_TOT'])


# In[34]:


result


# ### Exercise
# 
# Plot the linear model with the data.
