#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 13:46:24 2022

@author: jimmy
"""

""" 35. Write a Pandas program to create a TimeSeries to display all the Sundays of given year."""
import pandas as pd
import numpy as np

dataset_2 = pd.Series(pd.date_range('2020-01-01', periods=52, freq='W-SUN'))
print(f"All the Sundays of given year: \n{dataset_2}")

""" 36. Write a Pandas program to convert given series into a dataframe with its index as another column on the dataframe"""

char_list = list('ABCDEFGHIJKLMNOP')
num_arra = np.arange(8)
num_dict = dict(zip(char_list, num_arra))
num_ser = pd.Series(num_dict)
df = num_ser.to_frame().reset_index()
print(df.head())

""" 37. Write a Pandas program to stack two given series vertically and horizontally"""

dataset_3 = pd.Series(range(10))
dataset_4 = pd.Series(list('pqrstuvwxy'))

dataset_3.append(dataset_4)
output = pd.concat([dataset_3,dataset_4], axis = 1)
print(f"Stack two given series vertically and horizontally:\n{output}")

""" 38. Write a Pandas program to check the equality of two given series"""
nums1 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
nums2 = pd.Series([1, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series:")
print(nums1)
print(nums2)
print("Check 2 series are equal or not?")
print(nums1 == nums2)

""" 39.Write a Pandas program to find the index of the first occurrence of the smallest and largest value of a given series."""
nums = pd.Series([1, 3, 7, 12, 88, 23, 3, 1, 9, 0])
print("Index of the first occurrence of the smallest and largest value of the said series:")
print(f"{nums.idxmin()} \n{nums.idxmax()}")


""" 40 Write a Pandas program to check inequality over the index axis of a given dataframe and a given series."""

df_data = pd.DataFrame({'W':[68,75,86,80,None],'X':[78,75,None,80,86], 'Y':[84,94,89,86,86],'Z':[86,97,96,72,83]});
sr_data = pd.Series([68, 75, 86, 80, None]) 
print("Original DataFrame:")
print(df_data)
print("\nOriginal Series:")
print(sr_data)
print("\nCheck for inequality of the said series & dataframe:")
print(df_data.ne(sr_data, axis = 0))

