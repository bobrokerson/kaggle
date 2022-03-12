#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:08:36 2022

@author: jimmy
"""

""" 11. Write a Pandas program to sort a given Series."""
import pandas as pd

dataset = pd.Series(['100','200','python', '300.12','400']).sort_values()

print(f"Dataset sorted: \n{dataset}")

""" 12.Write a Pandas program to add some data to an existing Series"""

dataset_1 = dataset.append(pd.Series(['500','php']))

print(f"\nConcatenate dataset: \n{dataset_1}\n")

""" 13.Write a Pandas program to create a subset of a given series based on value and condition"""

dataset_2 = pd.Series([0,1,2,3,4,5,6,7,8,9,10])
val = int(input('Input data:'))
#dataset_3 = dataset_2.iloc[:6]

def equal(x,y):
    xy = x[x<y]
    return xy

print(equal(dataset_2,val))

""" 14.Write a Pandas program to change the order of index of a given series """

dataset_3 = pd.Series([1,2,3,4,5], index =['A','B','C','D','E'])
re_index = dataset_3.reindex(index =['B','A','C','D','E'])
print(f"\nReindex: \n{re_index}")

""" 15. Write a Pandas program to create the mean and standard deviation of the data of a given Series"""

dataset_4 = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])

print(f"\nMean: {dataset_4.mean()}")
print(f"\nSTD: {dataset_4.std()}")


