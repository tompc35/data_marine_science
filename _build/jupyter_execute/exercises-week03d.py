#!/usr/bin/env python
# coding: utf-8

# # Exercises
# 
# ### Probability
# 
# A newspaper article quotes a statistic about the relationship between the El Nino index and high precipitation in Southern California. A high precipitation winter is defined as being in the top 10% of all winters. According to the article, 75% of high precipitation winters in Southern California occur during El Nino years. El Nino events occur approximately every five years.
# 
# Based on this information, what is the probability of high precipitation occuring during an El Nino year?
# 
# ### Boolean logic
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
# 
# ### Pandas data frames
# 
# Create a list of unique station ID’s (“STNNBR”) found in the survey data. Call it `stns`. How many unique stations are there in the data? 
# 
# ### Exploratory analysis
# 
# * What scientific questions can be addressed with this data set?
# 
# * What relationships might occur between different variables?
# 
# * What differences might occur within the same variables, but at different locations or times?
# 
# * Create exploratory plots (one PDF, one scatter plot)
# 
# 
# ### Dataframe indexing
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
# ### Dataframe subsets 1
# 
# Select a subset of rows in the `df` DataFrame that contains data from a pressure range between 500 and 1000 dbar. How many rows did you end up with? What did your neighbor get?
# 
# ### Dataframe subsets 2
# 
# You can use the isin command in Python to query a DataFrame based upon a list of values as follows:
# ```
# df[df['STNNBR'].isin([listGoesHere])]
# ```
# Use the `isin` function to find all samples from station numbers 11 and 12.
# 
# ### Dataframe subsets 3
# 
# pH values are contained in the `df['PH_TOT']` DataArray of the WCOA data set.
# 
# Quality control flags for pH are contained in the `df['PH_TOT_FLAG_W']` DataArray.
# 
# World Ocean Circulation Experiment (WOCE) quality control flags are used: 
# 2 = good value,
# 3 = questionable value,
# 4 = bad value ,
# 5 = value not reported,
# 6 = mean of replicate measurements,
# 9 = sample not drawn.
# 
# 
# a. Create a new DataFrame called `dfsub1` that excludes all bad, questionable and missing pH values. Plot the probability density function for pH.
# 
# b. Create a new DataFrame called `dfsub2` that excludes all bad, questionable and missing pH and CTD oxygen values. Plot oxygen vs. pH.
# 
# 
# ### Linear regression
# 
# Create a linear model of pH as a function of CTD oxygen. Plot the linear model with the data.

# In[ ]:




