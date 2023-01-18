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

# In[3]:


get_ipython().run_line_magic('pinfo', 'fahr_to_celsius')


# To use the function:

# In[4]:


fahr_to_celsius(32)


# In[5]:


tempF = 212

tempC = fahr_to_celsius(tempF)
print('Temperature in Celsius is:',tempC)


# #### Multiple outputs

# In[6]:


def fahr_to_celsius_kelvin(temp_fahr):
    ''' Convert temperature from degrees F to Celsius and Kelvin '''
    temp_celsius = (temp_fahr - 32) * (5/9)
    temp_kelvin = temp_celsius + 273
    return temp_celsius,temp_kelvin


# In[7]:


fahr_to_celsius_kelvin(77)


# #### Specifying default values for inputs

# In[8]:


def fahr_to_celsius_kelvin(temp_fahr=32):
    ''' Convert temperature from degrees F to Celsius and Kelvin '''
    temp_celsius = (temp_fahr - 32) * (5/9)
    temp_kelvin = temp_celsius + 273
    return temp_celsius,temp_kelvin


# In[9]:


fahr_to_celsius_kelvin()


# __Exercises:__
#     
# * Create a function that takes a number as input, and returns the square of that number.
# * Create a function to calculate the standard deviation of an array (not using the `np.sqrt` function).

# ### Exercise: temperature conversion
# 
# Create a function that converts temperature from degrees Celsius to degrees Fahrenheit.
# 
# Use the function created above to convert the following array of temperature values from degrees F to degrees C. Avoid using a for loop.
# 
# ```python
# temps_f = np.array([50.5, 58.4, 62.3, 49.2])
# ``` 

# ### Exercise: Stokes law function
# 
# Stokes' law predicts the settling velocity (or "terminal velocity") of a sinking sphere, $v$ (units: m/s). The theoretical velocity is based on the radius of the particle, $r$ (units: m), the density of the particle  $\rho_p$ (units: kg/m$^3$), the density of the ambient fluid $\rho_f$, the dynamic viscosity of the ambient fluid $\mu$ (units: kg/(m*s)), and the acceleration due to gravity $g$ (units: m/s$^2$):
# 
# $$v = \frac{2}{9}\frac{(\rho_p-\rho_f)}{\mu}g r^2$$
# 
# Use the following template to create a function that calculates the velocity predicted by Stokes law:

# ``` python
# def stokes_law(r,rho_p,rho_f,mu,g):
#     # insert code here
#     return v
# ```

# Use your `stokes_law` function to estimate the settling velocity of the single-cell alga *Phaeocystis globosa*, assuming it is spherical. The radius of a typical cell is 46 $\mu m$ and the typical cell density is 1091 kg/m<sup>3</sup>. For standard seawater conditions (temperature = 10 deg C, practical salinity = 35) $\rho_f$ = 1025 kg/m<sup>3</sup>$, $\mu =$ 1.51 × 10<sup>−3</sup> kg/(m*s).
# 
# Source: L. Peperzak, F. Colijn, R. Koeman, W. W. C. Gieskes, J. C. A. Joordens, Phytoplankton sinking rates in the Rhine region of freshwater influence, Journal of Plankton Research, Volume 25, Issue 4, April 2003, Pages 365–383, https://doi.org/10.1093/plankt/25.4.365

# 10. Edit your function to use typical seawater values as defaults for  `rho_f` and `mu`.
