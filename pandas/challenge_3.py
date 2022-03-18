#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:08:36 2022

@author: jimmy
"""

""" 21.Write a Pandas program to find the positions of numbers that are multiples of 5 of a given series"""

import pandas as pd
import numpy as np

dataset_1 = pd.Series(np.random.randint(1, 10, 9))

out = np.where(dataset_1 % 5==0)

print(f"\ndataset: \n{dataset_1} \nPositions of numbers that are multiples of 5: {out}")


"""22.Write a Pandas program to extract items at given positions of a given series."""

dataset_2 = pd.Series(list('2390238923902390239023'))
element = [0, 2, 6, 11, 21]
result = dataset_2.take(element)
print(f"{dataset_2},\n{result}")


""" 23. Write a Pandas program to get the positions of items of a given series in another given series"""

dataset_3 = pd.Series(np.arange(1,11))
dataset_4 = pd.Series([1,3,5,7,10])
print(f"dataset: {dataset_3} \n{dataset_4}")
res = [pd.Index(dataset_3).get_loc(i) for i in dataset_4]

print(f"Positions of items of series2 in series1: {res}")

"""24. Write a Pandas program convert the first and last character of each word to upper case in each word of a given series"""

dataset_5 = pd.Series(['php','python','java','c#'])
#output = [pd.Series(dataset_5).lower(i) for i in dataset_5]
output = dataset_5.map(lambda x: x[0].upper() + x[1:-1] + x[-1].upper())
print(f"First and last character of each word to upper case: \n{output}")



""" 25. Write a Pandas program to calculate the number of characters in each word in a given series"""

dataset_6 = pd.Series(['php','python','java','c#'])
dataset_7 = dataset_6.str.title()
fin = dataset_7.map(lambda calc: len(calc))
print(f"\nDataset: \n{dataset_7} \n{fin}")









