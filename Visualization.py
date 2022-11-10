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


def getDataSet():
    '''
    This function retruns data after fetching data from web and read using pandas and save it in a dataframe.
    Selects specific rows data and validate data types.
    '''
    url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/UK.txt"
    s = requests.get(url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), delimiter='\s+', skiprows=(5), index_col=False)
    
    #Drop N/A data to clean data
    df.dropna()
    # Selecting specific years data for clean visualization
    df = df.loc[30:102]
    # Printing dataypes of dataframe to validate data.
    df.dtypes
    #Converting datatype from object to float64 so we can work with numerical data.
    df['win'] = df['win'].astype(dtype='float64')
    
    return df


df = getDataSet()




