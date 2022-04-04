#!/usr/bin/env python
# coding: utf-8

# # Spectral Analysis 
# 
# ## Math review - complex numbers
# 
# Complex numbers are used to represent numbers in 2 dimensional space. 
# 
# example 5+2$i$, where $i=\sqrt{-1}$
# 
# real part: $x$=5
# 
# imaginary part: $y$=2
# 
# $z$=5+2$i$
# 
# Complex numbers can be thought of as vectors in two dimensional space. In the formula above, $x$ and $y$ can be thought of as the components of a vector $z$. We can also think about complex numbers as vectors with a magnitude($r$) and angle/phase ($\phi$). Trigonometry can be used to describe the relationship between these two types of vector representation.
# 
# $x=rcos\phi$
# 
# $y=rsin\phi$
# 
# $r=|z|=\sqrt{x^2+y^2}$
# 
# $\frac{y}{x}=tan\phi$
# 
# $\phi=tan^-1(\frac{y}{x})$
# 
# $=rcos\phi+i(rsin\phi)$
# 
# $=r(cos\phi+isin\phi)$
# 
# $z=re^{i\phi}$ 
# 
# This final formula shows how the complex number can be expressed compactly in terms of its magnitude and angle. 
# 
# Although we often think of exponential functions as growth or decay, an exponential with an imaginary exponent describes oscillations (i.e. sines and consines). The literature on spectral analysis often uses this type of equation.

# ##### Complex Conjugate
# $z=x+iy$
# 
# $z^*=x-iy$
# 
# $|z|^2=zz^*$
# 
# $=(x+iy)(x-iy)$
#     
# $=x^2-ixy+ixy+y^2$
#     
# $=x^2+y^2$

# ## Terminology
# 
# ### Monochromatic signals
# 
# Monochromatic = "one color"
# 
# A wave with a single frequency (f=1/t)
# 
# Time series of a surface elevation variation $\eta(t)$
# 
# $\eta(t)=\eta_{max}cos(2\pi ft)$
# 
# $\eta(t)=\eta_{max}cos(2\pi ft-\phi)$
# 
# $\eta(t)=\alpha cos(2\pi ft)+\beta sin(2\pi ft)$
# 
# $\eta_{max}=\sqrt{\alpha^2+\beta^2}$
# 
# ### Non-monochromatic signals
# 
# $\eta(t)=\bar\eta + \eta_{max}cos(2\pi ft-\phi_1)+\eta_{max}cos(4\pi ft-\phi_2)+ \eta_{max}cos(6\pi ft-\phi_3)$
# 
# becomes
# 
# $\eta(t)=\bar\eta+\sum^3_{j=1}\eta_{max_j} cos(2\pi f j t-\phi_i)$
# 
# or 
# 
# $\eta(t)=\bar\eta+\sum^3_{j=1}[\alpha_j cos(2\pi f j t)+\beta_j(2\pi f j t)]$
# 
# An infinite number of sin waves can be added to each other to make any signal in existence. This includes both repeating waveforms and non repeating waveforms.
# 
# ### Practical Limitations
# - In practice we cannot fit an infinite set of sines and cosines to a time series that we collect in the ocean
# - With a limited set of discrete observations, only a limited set of frequencies can be fit to the data
# - The lowest frequency (longest period) also called the fundamental frequency 
# 
# $f_f=\frac{1}{t_{max}}$ where $t_{max}$ =record length
# 
# or
# 
# $f_f=\frac{1}{N\Delta t}$ where $\Delta t$ =sampling interval and $N$ is the number of samples.
# 
# 
# ## Fourier Analysis
# 
# Model a time series $y(t)$ with the "harmonics" of the fundamental frequency
# 
# $f_f, 2f_f, 3f_f, 4f_f...\frac{N}{2}f_f$
# 
# These frequencies range from the lowest frequency we measured (the fundamental frequency) to the highest frequency (the Nyquist frequency).
# 
# At each frequency $f_k$ the wave has variance:
# 
# $\sigma^2_{y_k}=\frac{1}{2}(\alpha^2_k+\beta^2_k)$
# 
# Total variance ove $y(t) =\frac{1}{2}y^2_{maxk}$
# 
# $\sigma^2_{y_{total}}= \frac{1}{2}\sum^{N/2}_{k=1}(\alpha^2_k+\beta^2_k)$
# 
# The waves with greater amplitude contribute more to the variance of the time series.
# 
# ## Discrete Fourier Analysis
# 
# The Fourier coefficients of a sequence, or time series, $y = [y_0,y_1,y_2,...,y_{N-1}]$ can be defined as
# 
# $Y_k=\sum^{N-1}_{n=0}y_ne^{-i2\pi kn/N}$
# 
# For each frequency, the Fourier coeffient is the sum of (all function values $\times$ sines and cosines) over all N.
# 
# The sum of (all function values x sines and cosines) is the same as computing the covariance between the function and sine/cosine waves.
# 
# In general, the Fourier coefficients are complex numbers which describe both the coefficients for both the sine and cosine waves.
# 
# Computing these sums for all fequencies gives a set of Fourier coefficients.
# 
# $Y_k =[Y_0,Y_1,Y_2,....Y_{N/2},......Y_{N-1}]$
# 
# The intuitive method of computing these coefficients would be to loop through all frequencies and compute the covaraince for each frequency. This requires $N^2$ operations.
# 
# The "fast Fourrier transform" (FFT) requires only $N\log(N)$ coperations
# 
# Inverse DFT gets the time series back to is original form
# $Y_n=\frac{1}{N}\sum^{N-1}_{n=0}y_ne^{i2\pi kn/N}$
# 
# The Discrete Fourier Transform and Inverse DFT may be shown with different scalings (i.e. there is not always a factor 1/N in the equation above). The form used varies by book and programming language. However, the equations should always be internally consists, so that the Inverse DFT always returns the original time series.

# In[ ]:




