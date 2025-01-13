#!/usr/bin/env python
# coding: utf-8

# # Multivariate regression tutorial: aragonite saturation state
# 
# Using data from the West Coast Ocean Acidification (WCOA) cruise, create two different multiple linear regression models to calculate aragonite saturation state ($\Omega_A$) between 30 and 300 dbar as a function of more commonly observed variables. This is similar to "Model 1" described in [the previous section](2-06b-implementing-multivariate-regression.ipynb), following [Juranek et al. (2009)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2009GL040778). Note that there are a couple of issues with this model that led Juranek et al. (2009) to select a different model: bias and multicollinearity.
# 
# Juranek, L. W., R. A. Feely, W. T. Peterson, S. R. Alin, B. Hales, K. Lee, C. L. Sabine, and J. Peterson, 2009: A novel method for determination of aragonite saturation state on the continental shelf of central Oregon using multi-parameter relationships with hydrographic data. Geophys. Res. Lett., 36, doi:10.1029/2009GL040778.
# 
# First import the necessary packages and load the data.

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
import pingouin as pg

import PyCO2SYS as pyco2


# In[2]:


filename07 = 'data/wcoa_cruise_2007/32WC20070511.exc.csv'
df07 = pd.read_csv(filename07,header=29,na_values=-999,
                  parse_dates=[[6,7]])


# We use the [PyCO2SYS](https://pyco2sys.readthedocs.io/en/latest/) package to calculate the carbonate system parameters. This gives us values for aragonite saturation state that we can put in our dataframe.

# In[3]:


c07 = pyco2.sys(df07['ALKALI'], df07['TCARBN'], 1, 2,
               salinity=df07['CTDSAL'], temperature=df07['CTDTMP'], 
                pressure=df07['CTDPRS']);
df07['OmegaA'] = c07['saturation_aragonite'];


# ## Model 1: Temperature, salinity, pressure, dissolved oxygen and nitrate:
# 
# * Temperature
# * Salinity
# * Pressure
# * Oxygen
# * Nitrate
# 
# $$\hat{\Omega}_A = c_{0} + c_{1} \times T + c_{2} \times S + c_{3} \times p + c_{4} \times O_2 + c_{5} \times N$$
# 
# First, create a subset of all good data between 30-300 dbar. 

# In[4]:


ii = ((df07['CTDPRS'] >= 30) & (df07['CTDPRS'] <= 300) &
      (df07['NITRAT_FLAG_W'] ==2) & (df07['PHSPHT_FLAG_W'] ==2) &
      (df07['CTDOXY_FLAG_W'] == 2) & (df07['CTDSAL_FLAG_W'] ==2) &
      (df07['TCARBN_FLAG_W'] == 2) & (df07['ALKALI_FLAG_W'] == 2) & 
      (df07['LATITUDE'] > 41) & (df07['LATITUDE'] < 48))


# In[5]:


df07sub = df07[ii]


# In[6]:


y = df07sub['OmegaA']


# Solve for the coefficients $\vec{c}$ in the least squares problem:
# 
# $$ \hat{y} = \textbf{X}\vec{c} $$ 
# 
# Create a 2-D array `X` that contains a column of all ones, and additional columns containing the explanatory variables. This 2-D array is called the "design matrix" and should have six columns. What are the explanatory variables in this case? 
# 
# * Approach: use `np.ones()` to create a 2-D array of correct size, then fill in the columns.

# In[7]:


k = 5 # number of predictor variables
N = len(df07sub['OmegaA']) # number of observations 


# In[8]:


N


# In[9]:


X = np.ones([N, k+1])


# In[10]:


np.shape(X)


# In[11]:


X[:,1] = df07sub['CTDTMP']
X[:,2] = df07sub['CTDSAL']
X[:,3] = df07sub['CTDPRS']
X[:,4] = df07sub['CTDOXY']
X[:,5] = df07sub['NITRAT']


# In[12]:


X


# Use `np.linalg.lstsq` to compute the set of coefficients, `c`.

# In[13]:


result = np.linalg.lstsq(X,y)


# In[14]:


result


# In[15]:


c = result[0]


# In[16]:


c


# Alternative solution using matrix multiplication:
# 
# $$\hat{c} = (\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\vec{y}$$

# In[17]:


c2 = np.linalg.inv(X.T@X)@X.T@y


# In[18]:


c2


# Now calculate the model values, $\hat{y}$.

# In[19]:


yhat = X@c


# ## Assessing the model for bias
# 
# Plot model vs. observations. Note the systematic underestimate at high and low values of $\Omega_A$. The residual plot shows this even more clearly.

# In[20]:


plt.figure()
plt.plot(y,yhat,'.')
xl = plt.xlim()
yl = plt.ylim()
plt.plot(xl, xl, 'k--')
plt.xlim(xl)
plt.ylim(yl)
plt.xlabel('observed $\Omega_A$')
plt.ylabel('modeled $\Omega_A$');


# Plot residuals vs. observations.

# In[21]:


plt.figure()
plt.plot(y, yhat-y,'.')
xl = plt.xlim()
plt.plot(xl,[0,0],'k--')
plt.xlim(xl)
plt.xlabel('observed $\Omega_A$')
plt.ylabel('residuals (modeled - observed)');


# ### Alternative approach using statsmodels
# 
# Use `statsmodels` to get a complete summary of regression statistics. Note that the coefficients are the same as those obtained using Numpy above.

# In[22]:


resultsm  = sm.OLS(y, X).fit()
print(resultsm.summary())


# In[23]:


resultsm.params


# In[24]:


c


# ### Confronting multicollinearity
# 
# In the output above, statsmodels gave a warning about a high *condition number* - this is an indicator of how much a small change to the matrix $\textbf{X}$ will change the solution to the least squares problem $\hat{c} = (\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\vec{y}$. It is a measure of the extent to which the columns in $\textbf{X}$ are linearly independent and closely scaled in magnitude. The same condition number can be calculated using Numpy.

# In[25]:


np.linalg.cond(X)


# Multiple collinearity can also be assessed by looking at the correlation matrix (R) or calculating the variance inflation factor (VIF).

# In[26]:


R = df07sub[['CTDTMP', 'CTDSAL', 'CTDPRS', 'CTDOXY', 'NITRAT']].corr()


# In[27]:


R


# In[28]:


VIF = 1/(1 - R**2)


# In[29]:


VIF


# ### Final model for aragonite saturation state
# 
# Due to issues with bias and multiple collinearity, the following alternative model proposed by Juranek et al. (2009). It is simpler and contains an interaction term.
# 
# 
# $ \hat{\Omega}_A = a_0 + a_1 \times (O - Oref) + a_2 \times (O - Oref) \times (T - Tref) $
# 
# An important question is whether this model can predict aragonite saturation state in different years. This model can be tested using an independent data set from later cruises that cover the same region.

# In[ ]:




