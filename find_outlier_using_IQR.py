import numpy as np


#  Detecting outlier using InterQuantile Range 75% - 25% values in a dataset

'''Arrange the data in increasing order
2. Caluculate first(q1) and third quartile(q3)
3. Find interquartile range (q3- q1)
4. Find lower bound q1*1.5
5. Find upper bound q3*1.5

Anything that lies outside of lower and upper bound is outlier'''



dataset= [11,10,12,14,12,15,14,13,15,102,12,14,17,19,107, 10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]


quantile1, quantile3 = np.percentile(dataset,[25,75])

print(quantile1,quantile3)

## find the IQR

iqr_value=quantile3 - quantile1
print(iqr_value)

## find the upper and lower bound value

lower_bound_val = quantile1 -(1.5 * iqr_value)
upper_bound_val = quantile3 +(1.5 * iqr_value)

print(lower_bound_val,upper_bound_val)

