#!/usr/bin/env python
# coding: utf-8

# # Analysis of variance (ANOVA)

# Test for a statistically significant difference between means of 3+ different groups
# 
# * Does not tell you which group is different
# * Requires the use of *post hoc* analysis to determine which means are different from each other
# 
# ## Fisher's "classic" one-way ANOVA
# 
# * J Populations (or "treatments")
# * N samples per population
# * $H_0: \mu_1 = \mu_2 = \mu_3 = \mu_4$
# * $H_a$: One mean will be different from any of the others
# 
# Three different types of CTDs in a water bath, each has four different measurements
# (does not require the same number of samples within each population)
# 
# Use the F-statistic: The ratio of the variances of two groups of samples taken from a normal distribution follows an *F* distribution
# 
# $$ F = \frac{s_1^2}{s_2^2}$$
# 
# The F distribution can be used to test whether variances are  significantly different. In the case of ANOVA, we want to test whether the variance of differences between different groups is larger than the variance within groups.
# 
# Sum of Squares Between: SSB = $\sum_{j=1}^J{N_j(\bar{y_j}-\bar{y})^2}$ where $\bar{y_j}$ is the mean of each population and $\bar{y}$ is the mean of all samples
# 
# Mean Square Between: MSB = $\frac{SSB}{J-1}$
# 
# $J-1$ is the degrees of freedom in calculating MSB.
# 
# Sum of Squares Within: SSW = $ \sum_{j=1}^J{\sum_{i=1}^{N_j}}({y_{ij}} - \bar{y}_j)^2$
# 
# Mean Square Within: MSW = $ \frac{SSW} {(\sum_{j=1}^J { N_j}) -J }$
# 
# $\sum_{j=1}^J ({ N_j} -J )$ is the degrees of freedom in calculating MSW. This is the total number of samples minus the number of groups.
# 
# F-Distribution: $F =\frac{MSB}{MSW}$
# 
# 
# The null hypothesis can be rejected if F is large. This is a one-tailed test, since small values of F do not lead to a rejection of the null hypothesis. The region of rejection is is above some critical level, which is determined by the confidence level and the degrees of freedon in the numerator and denominator.
# 
# ## Other flavors of ANOVA
# 
# ### Welch's ANOVA
# 
# Similar to the Welch's t-test, the Welch's ANOVA relaxes the assumption of equal variance between groups.
# 
# ### Repeated measures ANOVA
# 
# Use when the samples are not independent between groups, like when measuring the same subjects over different time points in an experiments.
# 
# ### Two-Way ANOVA
# 
# Use when you are comparing means and have two nomimal variables, or two categories of groups that you are comparing between. In this case there is also an interaction term, which tells you if the difference between groups in one category is modulated by the differences in groups between another category. Can be extended to $N$-way ANOVA for more nominal variables.
# 

# ## post-hoc tests and multiple comparisons
# 
# The ANOVA only tests the null hypothesis all of the means are equal. If you reject the null hypothesis, you will probably want to know which of the groups are significantly different. Your intuition may tell you to do pair-wise t-tests. That is the general idea behind post-hoc tests, but care needs to be taken to account for multiple comparisons. 
# 
# For example, if you do 20 different comparsons on data drawn from the same distribution you would expect to get at least one "significant" difference. 
# 
# ### Classic ANOVA 
# 
# * Fisher's LSD (least significant difference)
# 
# * Tukey HSD (honest significant difference)
# 
# ### Welch's ANOVA
# 
# * Games-Howell
# 
# ### Bonferroni correction 
# 
# The post-hoc tests above are designed specifically for ANOVA. Another common correction for multiple comparison is the Bonferonni correction. In that case, take the p-value you get and multiply it by the number of comparisons. This effectively sets a higher bar for statistical significance. In other words the Type I error rate is reduced.
# 

# ## Recommended reading ###
# 
# McDonald, J.H. 2014. Handbook of Biological Statistics (3rd ed.). Sparky House Publishing, Baltimore, Maryland. Freely available online at [www.biostathandbook.com](www.biostathandbook.com)

# In[ ]:




