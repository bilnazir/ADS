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
    '''This function retruns dataframe after fetching data from web and read using pandas and save it in a dataframe.
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
    
    '''This function plot a line chart using dataframe.
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
    
def plotBarChart():
    '''This function plot bar chart from the dataset using dataframe.
    Bar chart shows duration of sunlight in UK between 2000-2005 for all seasons.
    '''
    # loc function used to get data of specific years 2000-2005 from dataframe.
    df_bar = df.loc[81:86]
    x = np.arange(6)
    width = 0.2
    years = df_bar['year'].tolist()

    plt.figure(dpi=200)
    #To show main title of plot.
    plt.title('Barchart for Sunlight duration in UK')
    # x is used for grouped bar chart. x is the position of 1 bar.
    # x+0.2, x-0.2, x-0.4 these postion are used to show bar charts in groups.
    plt.bar(x, df_bar['spr'], width, label='Spring')
    plt.bar(x+0.2, df_bar['sum'], width, label='Summer')
    plt.bar(x-0.2, df_bar['aut'], width, label='Autmn')
    plt.bar(x+0.4, df_bar['win'], width, label='Winter')
    # xticks are used to show years on x-axis of the plot.
    plt.xticks(x, years)
    plt.yticks(np.arange(100,1000,200))
    # x-axis label
    plt.xlabel('Years')
    # y-axis label
    plt.ylabel('Sunlight Duration')
    # legend function is called to make labels visibles on the chart like Seanson names.
    plt.legend()
    plt.show()
    

def getDataForPieChart(df_pie):
    '''This function returns calculated data for pie charts using dataframe.
    
    Keyword arguments:
    df_pie -- dataframe required of specific years of the same dataset used in this file. 
    
    Returns
    -------
    numpy array of selected data for pie chart
    '''
    #Sum of all years data season wise and calculate thier percentage to show data on plots
    _win = np.sum(df_pie['win']) / np.sum(df_pie['ann'])*100
    _spr = np.sum(df_pie['spr']) / np.sum(df_pie['ann'])*100
    _sum = np.sum(df_pie['sum']) / np.sum(df_pie['ann'])*100
    _aut = np.sum(df_pie['aut']) / np.sum(df_pie['ann'])*100
    pie_array = np.array([_win, _sum, _spr, _aut])
    return pie_array
    

def plotPieChart():
    '''This function plots 2 pie charts presenting data from data sets.
    The first pie charts shows the comparison of sunlight duartion between all seasons of years 1951-1955.
    The second pie charts shows the comparison of sunlight duartion between all seasons of years 2015-2020.
    '''
    
    # loc function used to get data of years between 2015-2020.
    df_pie1 = df.loc[32:36]
    df_pie2 = df.loc[97:101]
    
    pie1 = getDataForPieChart(df_pie1)
    pie2 = getDataForPieChart(df_pie2)
    
    seasons = ['Winter', 'Summer', 'Spring', 'Autmn']
    explode = (0, 0, 0.1, 0)

    fig = plt.figure(figsize=(8, 4), dpi=144)

    ax1 = fig.add_subplot(121)
    ax1.pie(pie1, labels=seasons, autopct='%1.1f%%', shadow=True, explode=explode)
    ax1.set_title('Sunlight duration in UK (1951-1955)')

    ax2 = fig.add_subplot(122)
    ax2.pie(pie2, labels=seasons, autopct='%1.1f%%', shadow=True, explode=explode)
    ax2.set_title('Sunlight duration in UK (2015-2020)')



df = getDataSet()
plotLineChart()
plotBarChart()
plotPieChart()


