#!/usr/bin/env python
# coding: utf-8

# # Implementing linear regression in Python
# 
# Like many data analysis problems, there are a number of different ways to perform a linear regression in Python. This notebook shows a few different methods. The final method motivates a review of matrix multiplication, which will be helpful in the next section on multivariate regression.
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


filename07 = 'data/wcoa_cruise_2007/32WC20070511.exc.csv'
df07 = pd.read_csv(filename07,header=29,na_values=-999,parse_dates=[[6,7]])


# In[3]:


df07.keys()


# ## Linear regression: five methods in Python

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


# ### Method 1: Scipy

# In[8]:


result = stats.linregress(x[ii],y[ii])


# In[9]:


result


# In[10]:


result.slope


# Exercise: Draw the regression line with the data

# In[11]:


plt.figure()
plt.plot(x,y,'k.')
plt.plot(x,result.slope*x+result.intercept,'r-')


# ### Method 2: statsmodels

# Ordinary least squares fit using [statsmodels](https://www.statsmodels.org/).

# In[12]:


smres = smf.ols('NITRAT ~ PHSPHT',df07).fit()


# In[13]:


smres.summary()


# ### Method 3: pingouin

# In[14]:


pg.linear_regression(x[ii],y[ii])


# ### Method 4: Regression coefficients using numpy's polyfit function
# We can also use the `polyfit` function from numpy to calculate the coefficients of the line of best fit (minimizing the sum of square errors): 

# In[15]:


coefficients = np.polyfit(x[ii],y[ii],1)
print(coefficients)


# ### Method 5: Matrix form
# 
# In the next section, we'll consider solving for the coefficients of the linear fit using matrices. But first, let's do a quick review of matrix multiplication:
# 
# #### Review: Matrix Multiplication
# Suppose we have the following matrices:
# 
# $$ \textbf{A}= \begin{bmatrix} 1 & 2 & 3\\ 4 & 5 & 6 \end{bmatrix} $$
# 
# $$ \textbf{B} = \begin{bmatrix} 7 & 8\\ 9 & 10 \\ 11 & 12 \end{bmatrix} $$
# 
# What will be the matrix product $\textbf{AB}$?
# 
# To define matrices in Python, we define 2-d arrays as lists of lists wrapped in numpy's ```array``` function, for example:

# In[16]:


# define matrix A
A = np.array([[1, 2, 3], 
              [4, 5, 6]])

# define matrix B 
B = np.array([[7, 8], 
              [9, 10], 
              [11, 12]])


# We can check the dimensions of these array's using numpy's ```shape``` function:

# In[17]:


print('shape of A: ', np.shape(A))
print('shape of B: ', np.shape(B))


# Finally, we can multiply two arrays using numpy's ```dot``` function:

# In[18]:


np.dot(A,B)


# It is important to remember that matrix multiplication is not *commutative*, meaning $\textbf{AB}$ is generally not the same as $\textbf{BA}$. In this example, $\textbf{BA}$ gives us a different size matrix.

# In[19]:


np.dot(B,A)


# #### Review: Matrix Transpose
# 
# The *transpose* of a matrix $\textbf{A}^T$ has the same values as $\textbf{A}$, but the rows are converted to columns. One way to do this is with the `np.transpose` function.

# In[20]:


print(A)


# In[21]:


print(np.transpose(A))


# Another way is to use the `.T` method on a Numpy array.

# In[22]:


print(A.T)


# Note that the product $\textbf{A}^T\textbf{A}$ is a *square* matrix, which has the same number of rows and columns. 

# In[23]:


np.dot(A.T, A)


# #### Review: Matrix Inverse

# The concept of a matrix inverse is similar to the matrix of a single number. If we have a single value $b$, its inverse can be represented as $b^{-1}$. A value times its inverse is equal to 1.
# 
# $$b^{-1}b = 1$$

# Let's say we have a *square* matrix $\textbf{B}$ where the number of rows and columns are equal. The inverse $\textbf{B}^{-1}$ is the matrix that gives 
# 
# $$ \textbf{B}^{-1}\textbf{B} = \textbf{I} $$
# 
# where the *identity matrix* $\textbf{I}$ is a matrix that has all 0 values, except for 1 values along the diagonal from the upper left to the lower right. For example, a 3x3 identity matrix would be
# 
# $$ \textbf{I} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0  & 1  \end{bmatrix} $$

# This is called an *identity matrix* because $\textbf{B}\textbf{I} = \textbf{I}\textbf{B} = \textbf{B}$ for square matrices. This is analagous to $1b = b$ for single values.
# 
# In a linear algebra class, you might calculate $\textbf{B}^{-1}$ by hand, but in this class we will rely in Numpy to do it for us. Let's set up a $3 \times 3$ $\textbf{B}$ matrix.

# In[24]:


B = np.array([[1, 2, 1],
              [3, 2, 1],
              [1, 2, 2]])
print(B)


# The inverse $\textbf{B}^{-1}$ is

# In[25]:


np.linalg.inv(B)


# The product $\textbf{B}^{-1}\textbf{B}$ can be calculated as

# In[26]:


BinvB = np.dot(np.linalg.inv(B), B)
print(BinvB)


# If we round these values, we can see more clearly that this is nearly identical to the identity matrix $\textbf{I}$, with some very small round-off error.

# In[27]:


print(np.round(BinvB))


# For reference, an identity matrix can be created with the `np.eye` function

# In[28]:


print(np.eye(3))


# #### Formulating linear regression in matrix form
# 
# We can formulate regression in terms of matrices as
# 
# $$\begin{bmatrix} y_1\\ y_2\\ \vdots \\ y_N \end{bmatrix} = \begin{bmatrix} 1 & x_1\\ 1 & x_2\\ \vdots & \vdots\\ 1 & x_N \end{bmatrix} \begin{bmatrix} c_0\\ c_1\end{bmatrix} + \begin{bmatrix} \varepsilon_1\\ \varepsilon_2\\ \vdots \\ \varepsilon_N \end{bmatrix}$$
# 
# or
# 
# $$\vec{y} = \textbf{X}\vec{c} + \vec{\varepsilon}$$
# 
# Here, $\vec{\varepsilon}$ represents the vector of errors, or differences between the model and data values.
# 
# $$ \vec{\varepsilon} = \hat{y} - \vec{y} $$
# 
# To solve for the parameters c using matrix multiplication, we first need to fomulate the $\vec{y}$ and $\textbf{X}$ matrices

# In[29]:


# check to see that the y_subset is only 1-d (and won't work for matrix multiplication)
# print(np.shape(y_subset))

# define an (N, 1 matrix of the y values)
y_matrix = np.reshape(y[ii].ravel(),(len(y[ii]),1))

# print the matrix
print(y_matrix)

# print the shape of the matrix
print('shape of y: ', np.shape(y_matrix))


# In[30]:


# define a matrix X with a column of ones and a column of the x values
X = np.column_stack([np.ones((len(x[ii]),1)),
                     np.ravel(x[ii])])

# print the X matrix
print(X)

# print the shape of the X matrix
print(np.shape(X))


# Now that we have our matrices set up, let's return to our model equation in matrix form.
# 
# $$\hat{y} = \textbf{X}\vec{c}$$
# 
# We can multiply each side of the equation by the transpose
# 
# $$\textbf{X}^T\hat{y} = \textbf{X}^T\textbf{X}\vec{c}$$
# 
# then multiply each side by the inverse of $\textbf{X}^T\textbf{X}$
# 
# $$(\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\hat{y} = (\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\textbf{X}\vec{c}$$
# 
# which reduces to
# 
# $$(\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\hat{y} = \textbf{I}\vec{c}.$$
# 
# $$(\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\hat{y} = \vec{c}$$
# 
# giving us an expression for the vector of coefficents $\vec{c}$.

# Here $\hat{y}$ represents the vector of *model* values. With the vector of *data* values $\vec{y}$ we can solve for the coefficients that minimize the sum of square errors using the same equation:
# 
# $$\vec{c} = (\textbf{X}^T\textbf{X})^{-1}\textbf{X}^T\vec{y}$$
# 
# Using numpy, we can define the matrix components of the above equation and then run the calculation to find the coefficients:

# In[31]:


# calculate the transpose of the matrix X
XT = np.transpose(X)

# calculate the product of XT and X
XTX = np.dot(XT,X)

# calculate the inverse of XTX
XTX_inverse = np.linalg.inv(XTX)

# then calculate the products of XTX, XT and using two dot products
c = np.dot(XTX_inverse,np.dot(XT,y_matrix))

# print the coefficients
print(c)


# As a sanity check, we can double check that the coefficients are the same as those from numpy's ```polyfit``` function

# In[32]:


coefficients = np.polyfit(x[ii],y[ii],1)
print(coefficients)

