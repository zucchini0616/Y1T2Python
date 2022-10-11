import pandas as pd
import matplotlib.pyplot as plt

def dailysalesjan():

    my_dataframe = pd.read_csv('Jan20\Jan20.csv')
    my_dataframe['event_time'] = my_dataframe['event_time'].astype('string')
    print("ok")
    my_dataframe['event_time'] = my_dataframe['event_time'].str.split(r" ", expand=True)[0]
    plotthis = my_dataframe['event_time'].value_counts()
    return plotthis
    # print(my_dataframe['event_time'].unique())    

def dailysalesOct():

    my_dataframe = pd.read_csv('Oct19\Oct19.csv')
    my_dataframe['event_time'] = my_dataframe['event_time'].astype('string')
    print("ok")
    my_dataframe['event_time'] = my_dataframe['event_time'].str.split(r" ", expand=True)[0]
    plotthis = my_dataframe['event_time'].value_counts()
    return plotthis
    # print(my_dataframe['event_time'].unique())