#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:14:21 2022

@author: bilalnazir
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import requests


url="https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/UK.txt"
s=requests.get(url).content
df=pd.read_csv(io.StringIO(s.decode('utf-8')), delimiter='\s+', skiprows=(5), index_col=False)

df.dropna() #Drop N/A data to clean data
df = df.loc[30:102] # Selecting specific years data for clean visualization

df.dtypes # checking data types of all columns in dataframe. If all columns are valid to work with
df['win'] = df['win'].astype(dtype='float64') #Converting datatype from Object to float64 so we can work with numerical data


