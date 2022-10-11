import pandas as pd
import matplotlib.pyplot as plt

def dailysalesjan():

    my_dataframe = pd.read_csv('data\Jan20.csv')
    my_dataframe['event_time'] = my_dataframe['event_time'].astype('string')
    
    my_dataframe['event_time'] = my_dataframe['event_time'].str.split(r" ", expand=True)[0]
    plotthis = my_dataframe['event_time'].value_counts()
    return plotthis
    # print(my_dataframe['event_time'].unique())    

def dailysalesOct():

    my_dataframe = pd.read_csv('data\Oct19.csv')
    my_dataframe['event_time'] = my_dataframe['event_time'].astype('string')
 
    my_dataframe['event_time'] = my_dataframe['event_time'].str.split(r" ", expand=True)[0]
    plotthis = my_dataframe['event_time'].value_counts()
    return plotthis
    # print(my_dataframe['event_time'].unique())