#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:08:36 2022

@author: jimmy
"""

""" 17.Write a Pandas program to get the items of a given series not 
present in another given series"""

import pandas as pd
dataset_1 = pd.Series([1,2,3,4,5])
dataset_2 = pd.Series([2,4,6,8,10])

print(f"sr1: \n{dataset_1},\nsr2: \n{dataset_2}")

output = dataset_1[~dataset_1.isin(dataset_2)]
print(output)

""" 18.Write a Pandas program to compute the minimum, 25th percentile, median, 75th, and maximum of a given series"""

import numpy as np

dataset_3 =np.random.RandomState(100)
dataset_4 = pd.Series(dataset_3.normal(10,4,20))
print(f"\nData about dataset: \n{dataset_4.describe()}")

output = np.percentile(dataset_4, q=[0, 25, 50, 75, 100])
print(f"Second option: {output}")


""" 19. Write a Pandas program to calculate the frequency counts of each unique value of a given series"""

dataset_5 = pd.Series(np.take(list('0123456789'), np.random.randint(10, size=40)))
print(dataset_5)
out = dataset_5.value_counts()
print(out)

""" 20. Write a Pandas program to display most frequent value in a given series and replace everything else as 'Other' in the series"""

dataset_6 = pd.Series(np.take(list('01234'), np.random.randint(5, size=15)))
print(dataset_6)
print(f"\n{dataset_6.value_counts()}")

outputs = dataset_6[~dataset_6.isin(dataset_6.value_counts().index[:1])] = 'other'

print(dataset_6)






