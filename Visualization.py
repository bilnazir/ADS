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
    This function retruns dataframe after fetching data from web and read using pandas and save it in a dataframe.
    Selects specific rows data and validate data types.
    '''
    url = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Sunshine/date/UK.txt"
    s = requests.get(url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), delimiter='\s+', skiprows=(5), index_col=False)
    
    # Drop N/A data to clean data
    df.dropna()
    # Selecting specific years data for clean visualization (Years 1949-2021) 
    df = df.loc[30:102]
    # Printing dataypes of dataframe to validate data.
    df.dtypes
    #Converting datatype from object to float64 so we can work with numerical data.
    df['win'] = df['win'].astype(dtype='float64')
    
    return df

def plotLineChart():
    '''
    This function plot a line chart using dataframe.
    Line plot represents graphical visual of sunlight duration in UK bewteen 1947 - 2021.
    '''
    
    
    fig, axs = plt.subplots(2, 2, figsize=(8, 4))
    # Title for line plot
    fig.suptitle("Line plot for sunlight duration in UK")
    
    # First subplot on topleft.
    axs[0, 0].plot(df['year'], df['win'])
    axs[0, 0].set_title("Winter")
    axs[0, 0].set_xlim(1949,2021)
    # Second subplot on topright.
    axs[0, 1].plot(df['year'], df['spr'], 'tab:orange')
    axs[0, 1].set_title("Spring")
    axs[0, 1].set_xlim(1949,2021)
    axs[0, 1].yaxis.set_label_position("right")
    axs[0, 1].yaxis.tick_right()
    # Third subplot on bottom left.
    axs[1, 0].plot(df['year'], df['sum'], 'tab:green')
    axs[1, 0].set_title("Summer")
    axs[1, 0].set_xlim(1949,2021)
    # Fourth subplot on bottom right.
    axs[1, 1].plot(df['year'], df['aut'], 'tab:red')
    axs[1, 1].set_title("Autumn")
    axs[1, 1].set_xlim(1949,2021)
    axs[1, 1].yaxis.set_label_position("right")
    axs[1, 1].yaxis.tick_right()
    # x-axis and y-axis labels for all subplots
    for ax in axs.flat:
        ax.set(xlabel='Years', ylabel='Sunlight Duration')
        # Hide left subplots y-axis labels to make visuals better.
        ax.label_outer()

    fig.tight_layout()


df = getDataSet()
plotLineChart()




