#!/usr/bin/env python
# coding: utf-8

# # Example: modeling tropical storm counts
# 
# The number of tropical storms is an example of a variable that is not expected to be normally distributed. Counts cannot be negative, are often skewed and tend to follow a Poisson distribution.
# 
# This example follows the general approach of [Villarini et al. (2010)](https://journals.ametsoc.org/view/journals/mwre/138/7/2010mwr3315.1.xml) in using Poisson regression to model the number of tropical storms based on climate indices.
# 
# The goal of Poisson regression is to model a rate of occurrence, $\Lambda_i$, where the rate changes for each observation $i$. This model can be expressed as a generalized linear model (GLM) with a *logarithmic link function*.
# 
# $$\log(\Lambda_i) = \beta_0 + \beta_1 x_{1i} + \beta_2 x_{2i} + ... + \beta_n x_{ki}$$
# 
# which is the same as
# 
# $$\Lambda_i = \exp(\beta_0 + \beta_1 x_{1i} + \beta_2 x_{2i} + ... + \beta_n x_{ki})$$
# 
# This is a model for the rate of occurrence $\Lambda_i$ as a function of $k$ predictor variables. In this example, the rate of occurrence $\Lambda_i$ is the number of storm counts per year and each climate index is a predictor variable. 
# 
# * The logarithmic link function is useful because $\log(\Lambda_i)$ can be positive or negative, but $\Lambda_i$ must be positive
# 
# * If the data being modeled is a standard Poisson random variable, the model simplifies to $\Lambda_i = \exp({\beta_0})$

# In[1]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf


# We use a special function to load the climate indices from NOAA.

# In[2]:


def read_psl_file(psl_file):
    '''
    Read a data file in in NOAA Physical Sciences Laboratory (PSL) format
    
    Input: String containing the path to a PSL data file
    Returns: Pandas dataframe with monthly data in columns and the year as the index
    
    For a description of the PSL format see: https://psl.noaa.gov/gcos_wgsp/Timeseries/standard/
    '''
    
    f = open(psl_file, "r")
    all_lines = f.readlines()
    start_year = all_lines[0].split()[0]
    end_year = all_lines[0].split()[1]

    for i in range(1,len(all_lines)):
        stri = all_lines[i].find(end_year)
        if stri>=0:
            end_index = i

    missing_val = float(all_lines[end_index+1])
    nrows = int(end_year)-int(start_year)+1
    df = pd.read_csv(psl_file,skiprows=1,nrows=nrows,sep='\s+',header=None,na_values=missing_val)
    df = df.rename(columns={0:'year'})
    df = df.set_index('year',drop=True)
    
    return df


# In[3]:


dfsoi = read_psl_file('data/tropical-storms/soi.data')
dftna = read_psl_file('data/tropical-storms/tna.data')
dfnao = read_psl_file('data/tropical-storms/nao.data')


# Load the tropical storm data.

# In[4]:


dftrop = pd.read_csv('data/tropical-storms/tropical.txt',sep='\t')
dftrop = dftrop.set_index('Year',drop=False)


# Tropical storms do not happen in winter, so we average the climate indices during the relevant months.

# In[5]:


dftrop['SOI'] = dfsoi.loc[:,5:6].mean(axis=1)
dftrop['TNA'] = dftna.loc[:,5:6].mean(axis=1)
dftrop['NAO'] = dfnao.loc[:,5:6].mean(axis=1)


# ##### Exercises
# * How would you find the NAO averaged over July-September?
# * How would you find the NAO for years 2010-2020, averaged over July-September?
# * How would you use `dfnao.iloc` to achieve the same result?

# Drop all rows with any NaN values.

# In[6]:


df = dftrop.dropna()


# In[7]:


df


# Histogram of the named storm counts.

# In[8]:


plt.figure()
df['NamedStorms'].hist()


# Poisson distribution - model as a constant

# In[9]:


result = smf.glm(formula='NamedStorms ~ 1',
                 data=df,
                 family=sm.families.Poisson()).fit()
result.summary()


# In[10]:


k = np.arange(0,30)
mu = np.exp(result.params.Intercept)
pmf_poisson = stats.poisson.pmf(k,mu)

plt.figure()
df['NamedStorms'].hist(density=True)
plt.plot(k,pmf_poisson)


# Poisson regression model, including a linear temporal trend.

# In[11]:


result = smf.glm(formula='NamedStorms ~ Year + NAO + SOI + TNA',
                 data=df,
                 family=sm.families.Poisson()).fit()
result.summary()


# In[12]:


beta = result.params


# In[13]:


beta


# #### Exercises
# * Create a Python variable `y` that contains the observed count data.
# * Create a Python variable `yhat` that contains the modeled count data (use the parameters in `beta`).
# * Make plots comparing the observed and modeled counts.
