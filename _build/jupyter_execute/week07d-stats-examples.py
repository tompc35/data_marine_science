#!/usr/bin/env python
# coding: utf-8

# ## Statistics example problems
# 
# [1. ANOVA - geological example](#1.-ANOVA-geological-example)
# 
# [2. Non-parametric tests](#2.-Non-parametric-tests)

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import pingouin as pg


# ### 1. ANOVA geological example
# 
# #### a. Implementation
# 
# Data come from Table 10.1 of McKillup and Dyar, Geostatistics Explained, Cambridge University Press, 2010 (excerpt available on class Google Drive). Values represent the weight percent of MgO present in tourmalines from three locations in Maine. 
# 
# Use two different methods to test whether there is a significant difference in the mean MgO content between the three different sites.
# 
# ##### Method 1: Scipy

# In[2]:


df = pd.read_csv('data/MgO_example/MgO_Maine.csv') # dataframe


# In[3]:


df


# In[4]:


stats.f_oneway(df['Mount Mica'],df['Sebago Batholith'],df['Black Mountain'])


# ##### Method 2: Pingouin

# In[5]:


df2 = pd.read_csv('data/MgO_example/MgO_Maine_list.csv')


# In[6]:


df2


# In[7]:


pg.anova(data=df2,dv='MgO',between='Location')


# ##### Post-hoc test

# In[8]:


pg.pairwise_tukey(data=df2,dv='MgO',between='Location')


# #### b. ANOVA interpretation
# 
# Write a summary of your interpretation of the statistical results conducted above. Address the following questions.
# 
# * What is the null hypothesis being tested?
# * Should the null hypothesis be accepted or rejected?
# * What does the post-hoc test tell you?

# 

# ### 2. Non-parametric tests

# #### a. Wilcoxon signed-rank test: implementation
# 
# This example uses data from:
# http://www.biostathandbook.com/wilcoxonsignedrank.html
# 
# The data are observations of aluminum content in 13 different poplar clones in a polluted area. The scientific question is whether there is a significant change in the aluminum content between August and November.

# In[9]:


df_al = pd.read_csv('data/wilcoxon_example/Al_content.csv',
                   delimiter='\t')


# In[10]:


df_al


# In[11]:


plt.figure()
plt.hist(df_al['November']);


# In[12]:


stats.skewtest(df_al['November'])


# In[13]:


stats.normaltest(df_al['November'])


# In[14]:


stats.wilcoxon(df_al['August'],df_al['November'])


# #### b. Interpretation
# 
# Under what situations are non-parametric statistics useful? What are the potential drawbacks in using non-parametric statistics when a parametric approach is justified?

# 
