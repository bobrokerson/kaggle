#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:08:36 2022

@author: jimmy
"""


""" 31. Write a Pandas program to compute the Euclidean distance between two given series"""

import pandas as pd
from scipy.spatial import distance
import numpy as np

dataset = pd.Series([1,2,3,4,5,6,7,8,9,10])
dataset_1 = pd.Series([11,8,7,5,6,5,3,4,7,1])
print(f"{dataset}, \n{dataset_1}")
distance = distance.euclidean(dataset, dataset_1)
distance_2 = np.linalg.norm(dataset-dataset_1)
print(f"Euclidean distance between two said series: {distance.round(3)}  \nLinalg option: {distance_2.round(3)}")

""" 32.Write a Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series"""

dataset_2 = pd.Series([1,8,7,5,6,5,3,4,7,1])

temp = np.diff(np.sign(np.diff(dataset_2)))
result = np.where(temp == -2)[0] + 1
print(f"Positions of the values surrounded by smaller values on both sides: {result}")

""" 33. Write a Pandas program to replace missing white spaces in a given string with the least frequent character"""

str1 = 'abc def abcdef icd'
print(str1)
ser = pd.Series(list(str1))
element_freq = ser.value_counts()
print(element_freq)
current_freq = element_freq.dropna().index[-1]
result = "".join(ser.replace(' ', current_freq))
print(result)


""" 34. Write a Pandas program to compute the autocorrelations of a given numeric series."""
dataset_4 = pd.Series(np.arange(15) + np.random.normal(1, 10, 15))
print(F"Original series: {dataset_4}")

autocorrelations = [dataset_4.autocorr(i).round(2) for i in range(11)]
print("\nAutocorrelations of the said series:")
print(autocorrelations[1:])


