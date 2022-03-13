#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 23:08:36 2022

@author: jimmy
"""


""" 26.Write a Pandas program to compute difference of differences between consecutive numbers of a given series. """
import pandas as pd

dataset = pd.Series([1,3,5,8,10,11,15])
dataset_1 = dataset.diff()
dataset_2 = dataset_1.diff()

print(f"{dataset} \n{dataset_1.tolist()} \n{dataset_2.tolist()}")
print(dataset.tolist())

""" 27. Write a Pandas program to convert a series of date strings to a timeseries"""

dataset_3 = pd.Series(['01 Jan 2015','10-02-2016','20180307','2014/05/06','2016-04-12','2019-04-06T11:20'])
dataset_3_conv = pd.to_datetime(dataset_3)
print(f"{dataset_3}, \n{dataset_3_conv}")

"""28. Write a Pandas program to get the day of month, day of year, week number and day of week from a given series of date strings."""
from dateutil.parser import parse

dataset_5 = dataset_3.map(lambda x: parse(x))
dataset_day = dataset_5.dt.day.tolist()
dataset_month = dataset_5.dt.month.tolist()
dataset_dayofyear = dataset_5.dt.dayofyear.tolist()
dataset_weekofyear = dataset_5.dt.isocalendar().week.tolist()
dataset_weekday = dataset_5.dt.day_name().tolist()


print(f"{dataset_5}, \nDay of month: {dataset_day}, \nMonth: {dataset_month}, \nDay of year: {dataset_dayofyear}, \nWeek number: {dataset_weekofyear}, \nDay of week: {dataset_weekday}")

""" 29. Write a Pandas program to convert year-month string to dates adding a specified day of the month"""

dataset_6 = pd.Series(['Jan 2015','Feb 2016','Mar 2017','Apr 2018','May 2019'])
dataset_7 = pd.to_datetime(dataset_6) 
dataset_8 = dataset_6.map(lambda x: parse('05'+x))
print(f"{dataset_8}")

""" 30. Write a Pandas program to filter words from a given series that contain atleast two vowels"""
from collections import Counter
dataset_9 = pd.Series(['Red','Green','Orange','Pink','Yellow','White'])
output = dataset_9.map(lambda x:sum([Counter(x.lower()).get(i, 0) for i in list('aeiou')]) >= 2)

print(f"{dataset_9[output]}")




