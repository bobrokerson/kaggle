#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:38:47 2022

@author: jimmy
"""

# Pandas Data Series

import pandas as pd

"""1.Write a Pandas program to create and display a one-dimensional 
array-like object containing an array of data using Pandas module
"""
data = [2,4,8,16]

data_frame = pd.DataFrame(data)
data_series = pd.Series(data)
print(f"{data_series}, table description")


"""2.Write a Pandas program to convert a Panda module Series to Python 
list and it's type
"""
update_data = data_series.tolist()
print(f"convert pd.series to list: {update_data}", type(update_data))



"""3. Write a Pandas program to add, subtract, multiple and divide
 two Pandas Series. """

dataset_1 = pd.Series([2,4,6,8,10],index =['a','b','c','d','e'])
dataset_2 = pd.Series([1,3,5,7,9],index =['a','b','c','d','e'])

sub = dataset_1.subtract(dataset_2)
print(f"Subtract: \n{sub}")

dev = dataset_1.divide(dataset_2).round(4)
print(f"Divide: \n{dev}")

mul = dataset_1.multiply(dataset_2)
print(f"Multiply: \n{mul}")

add = dataset_1.add(dataset_2)
print(f"Add: \n{add}")


"""
4.Write a Pandas program to compare the elements of the two Pandas Series
"""
dataset_3 = pd.Series([2, 4, 6, 8, 10, 0])
dataset_4 = pd.Series([1, 3, 5, 7, 10, 0])

compare = dataset_3.compare(dataset_4)
print(f"Compare: {compare}")

def compare(x,y):
    print('\n Compare two dataset: \n',x==y)
    print('\n Greater than: \n', x>y)
    print('\n Less than \n',x<y)
    return

compare(dataset_3,dataset_4)


"""5. Write a Pandas program to convert a dictionary to a Pandas series """

dictionary = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}

result  = pd.Series(dictionary)
print(f"Convert dictionary to  pd.Series: \n{result}, done")


""" 6.Write a Pandas program to convert a NumPy array to a Pandas series"""

import numpy as np

arr = np.array([10,20,30,40,50])
result_arr = pd.Series(arr)
print(f"\nConvert array Numpy to  pd.Series: \n{result_arr}, done")

""" 7. Write a Pandas program to change the data type of given a column or a Series"""

dataset_5 = pd.Series([100,200,'python',300.12,400], 
                      index = ['position_1','position_2','position_3','position_4','position_5'])
                 
out = pd.to_numeric(dataset_5, errors='coerce')

print(f"\n{out}")

"""8. Write a Pandas program to convert the first column of a DataFrame as a Series"""

dataset_6 = pd.DataFrame({'col1':[1,2,3,4,7,11],
                          'col2':[4,5,6,9,5,0], 
                          'col3':[7,5,8,12,1,11]})
output = dataset_6['col1'].squeeze()
print(f"\n{output}")

""" 9. Write a Pandas program to convert a given Series to an array """

dataset_7 = pd.Series([100,200,'python',300.12,400])
#data_arr = dataset_7.array
ata_arr_1 = np.array(dataset_7.values.tolist())

print(f"\nConvert pd.series to array:{ata_arr_1}")


""" 10. Write a Pandas program to convert Series of lists to one Series"""

dataset_8 = pd.Series([['Red', 'Green', 'White'],['Red', 'Black'],['Yellow']])
print(f"\n{dataset_8}")

solution = dataset_8.apply(pd.Series).stack().reset_index(drop=True)
print(f"\nSolution: \n{solution}")

# I do this exercises just refresh my brain:)
 