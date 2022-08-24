# Data Analysis Techniques in Marine Science

An introductory resource for analyzing oceanographic data. Fundamental concepts in sampling and statistics are combined with hands on practice in scientific programming with Python.

![course banner image](images/course-image.png)

<!--These course notes are in Jupyter Notebooks. They can be viewed as static web pages on Github or run interactively on Binder at https://mybinder.org/v2/gh/mlmldata2020/course-notes/master

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mlmldata2020/course-notes/master)-->

## Software

* [Git reference](git-reference/README.md)

* [Installing software](software-installation/README.md)

## Course Schedule

### Week 1
* [Introduction to sampling and statistics](week01-introduction.ipynb)
* [The command line and shell scripts - Software Carpentry tutorial](https://swcarpentry.github.io/shell-novice/)

### Week 2

* [Probabilities and Distributions](week02-probability-and-distributions.ipynb)
* [Python Introduction](week02b-python-intro.ipynb)
* [Exercises - Python Introduction](week02c-exercises-python-intro.ipynb)

### Week 3

* [Modeling, sampling, confidence intervals](week03a-modeling-sampling.ipynb)
* [Boolean logic in Python](week03b-boolean.ipynb)
* [Cruise data analysis using Pandas](week03c-cruise-data-analysis.ipynb)
* [Exercises](week03d-exercises.ipynb)

### Week 4

* [Hypothesis testing, power analysis](week04a-hypothesis-power.ipynb)
* [Loops in Python](week04b-loops.ipynb)
* [Python functions](week04c-python-functions.ipynb)
* [Exercises](week04d-exercises.ipynb)

### Week 5

* [Correlation, general least squares regression](week05a-corr-regress-least-squares.ipynb)
* [Implementing linear regression in Python](week05b-wcoa-cruise-regression.ipynb)
* [Conditional execution](week05c-conditional-execution.ipynb)
* [Exercises](week05d-exercises.ipynb)

### Week 6
* [Multivariate regression](week06a-multivariate-regression.ipynb)
* [Python modules](week06b-python-modules.ipynb)

### Week 7   
* [Analysis of variance (ANOVA)](week07a-anova.ipynb)
* [Non-parametric statistical tests](week07b-nonparam.ipynb)
* [The generalized linear model](week07c_generalized_linear_model.ipynb)
* [Statistics example problems](week07d-stats-examples.ipynb)
* [Example: comparing temperature in three regions](week07e-example-comparing-wcoa-temperature)

### Week 8
* [Error propagation](week08a-error-propagation.ipynb)
* [Poisson regression example](week08b-poisson-regression-tropical-storms.ipynb)
* [Optimization and nonlinear modeling](week08c-optimization.ipynb)
* [Population growth and optimizing exponential fits](week08d-us-population-example.ipynb)

### Week 9
* [Principal component analysis (PCA) and empirical orthoginal functions](week09a-PCA-EOF.ipynb)
* [Multidimensional scaling analysis](week09b-MDS.ipynb)
* [Example: NDBC wind](week09c-ndbc-wind.ipynb)
* [Example: Monterey Bay Kelp PCA](week09d-monterey_bay_kelp.ipynb)

### Week 10
* [Week 10 - Spectral analysis](week10a-spectral-analysis.ipynb)
* [Week 10 Lab - Elkhorn Slough spectral analysis - Part 1](week10b-lobo-spectral.ipynb)

### Week 11
* [Week 11 Lab - Elkhorn Slough spectral analysis - Part 2](week11a-lobo-spectral-part2.ipynb)

### Week 12
* [Week 12 - Spatial analysis](week12a-spatial-analysis.ipynb)
* [Week 12 - Interpolation](week12b-interpolation.ipynb)
* [Week 12 - Mapping examples](week12c-mapping-intro.ipynb)

### Week 13
* [Week 13 - Convolution and filtering](week13a-filtering.ipynb)
* [Week 13 - Image analysis](week13b-image-analysis.ipynb)

### Week 14
* [Week 14 - Python packages](week14-python-packages.ipynb)


<!--*

* [Week 5 - Correlation, general least squares regression](week05a-corr-regress-least-squares.ipynb)

* [Week 5 Lab - Conditional execution](week05b-conditional-execution.ipynb)

* [Week 5 Lab - Python modules](week05c-python-modules.ipynb)

* [Week 6 - ANOVA, non-parametric statistics](week06a-anova-nonparam.ipynb)

* [Week 6 - The generalized linear model](week06b_generalized_linear_model.ipynb)

* [Week 6 Lab - WCOA cruise comparison and linear regression methods](week06c_wcoa_cruise_comparison.ipynb)

* [Week 6 Lab - GM and multiple regression workbook](week06d-GM-regression-multiple-regression-workbook.ipynb)

* [Week 7 - Error propagation](week07a-error-propagation.ipynb)

* [Week 7 - Optimization](week07b-optimization.ipynb)

* [Week 7 Lab - Stats examples](week07c-stats-examples.ipynb)

* [Week 7 Lab - Comparing regional temperatures](week07d-example-comparing-wcoa-temperature.ipynb)

* [Week 7 Lab - Poisson regression](week07e-poisson-regression-tropical-storms.ipynb)

* [Week 8 - Principal Component Analysis/Empirical Orthogonal Functions](week08a-PCA-EOF.ipynb)

* [Week 8 - Multi-Dimensional Scaling Analysis](week08b-MDS.ipynb)

* [Week 8 Lab - Population growth and optimizing exponential fits](week08c-us-population-example.ipynb)

* [Week 8 Lab - Python packages](week08d-python-packages.ipynb)

* [Week 9 - Spectral analysis](week09a_spectral_analysis.ipynb)

* [Week 9 Lab - NDBC wind](week09b-ndbc-wind.ipynb)

* [Week 9 Lab - Monterey Bay Kelp PCA](week09c-monterey_bay_kelp.ipynb)

* [Week 10 Lab - Elkhorn Slough spectral analysis - Part 1](week10a_lobo_spectral.ipynb)

* [Week 11 Lab - Elkhorn Slough spectral analysis - Part 2](week11a_lobo_spectral_part2.ipynb)

* [Week 11 - Spatial analysis](week11b-spatial-analysis.ipynb)

* [Week 11 - Interpolation](week11c-interpolation.ipynb)

* [Week 11 - Filtering](week11d-filtering.ipynb)

* [Week 12 - Mapping examples](week12a-mapping-intro.ipynb)

* [Week 12 - Image analysis](week12b-image-analysis.ipynb)

<!--
* [Week 4 - Power analysis](week04a-power-analysis.ipynb)

* [Week 3 Lab - WCOA cruise comparison](week03c_wcoa_cruise_comparison.ipynb)

* [Week 4 Lab - Linear regression examples](week04d-linear-regression-three-methods.ipynb)

* [Week 5 - The generalized linear model](week05a_generalized_linear_model.ipynb)

* [Week 6 - Optimization](week06b-optimization.ipynb)



* [Week 9 Lab - Pacific Decadal Oscillation and autocorrelation](week09b_correlation_function_pdo.ipynb)



* [Week 11 - Convolution, filtering and image analysis](week11a_filtering_image_analysis.ipynb)

* [Week 11 Lab - Mapping and projections](week11b_mapping_intro.ipynb)

#### Extras

* [Spatial analysis](x-spatial-analysis.ipynb)

* [Error propagation](x-error-propagation.ipynb)

* [Least squares harmonic analysis](x-least-squares-harmonic-fit.ipynb)

* [Modeling introduction, NPZ ecosystem model](x-modeling-and-NPZmodel.ipynb)


<!--

* [Week 4 Lab - Oceanographic cruise data](week04b-cruise-data-analysis.ipynb)

* [Week 5 - Multiple regression, matrices](week05a-multiple-regression-matrices.ipynb)

* [Week 5 Lab - Multiple regression and transformations example](week05b-mult-regression-example.ipynb)

* [Week 6 - Optimization and interpolation](week06a-optimization-interpolation.ipynb)

* [Week 6 Lab - Population growth and optimizing exponential fits](week06b-us-population-example.ipynb)

* [Week 6 Tutorial - Git](week06c-git-tutorial.ipynb)

* [Week 9 Lab - Mapping and projections](week09c_mapping_intro.ipynb)

* [Week 11 - Spatial analysis](week11-spatial-analysis.ipynb)

-->
