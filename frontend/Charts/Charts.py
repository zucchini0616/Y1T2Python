#####################################
#             Python Team4          #
#           Zi Bin,Shing,Jav        #
#####################################

import csv
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

##### Code by Zibin  #####
def category(db):
    df = pd.DataFrame(db)

    cat = df['category_code']
    accessories = cat.str.contains('accessories')
    apparel = cat.str.contains('apparel')

    #df['category_code'] = np.where(accessories, 'accessories',
            #                             np.where(apparel, 'apparel',
                        #                        cat.str.replace('.', ' ')))
                                                
    #df['category_code'].value_counts()[-1:-5].plot(kind='bar')
    df['category_code'] = df['category_code'].str.split('.').str[0]
    trythis = df['category_code'].value_counts().nlargest(5).sort_values(ascending=False)
    st.bar_chart(trythis)
# per month
##### Code by Zibin  #####
##### Code by Shing  #####
def shing1(df):
    
    # df = pd.read_csv(r"C:\users\shing\Desktop\INF1002 Project\mergedDatafilter.csv")
    df = df.dropna()
    df = df.drop(columns=['event_type'])
    df = df.drop(columns=['category_code'])
    df = df.drop(columns=['brand'])
    df['event_time'] = df['event_time'].str[:7]

    df = df.groupby([df.event_time])["price"].sum()
 
    # print(df)

    # st.bar_chart(df.event_time.dt.to_period('M').dt.strftime('%m/%Y').unique(),dfByMonth)
    st.bar_chart(df)
##### Code by Shing  #####

##### Code by Jav  #####
def jav1(df):
   

    df['category_code'] = df['category_code'].astype('string')
    df['category_code'] = df['category_code'].str.split(".", expand=True)[0]
    df = df.groupby('category_code')['price'].agg(['sum']).sort_values('sum', ascending= False)[:5]
    st.bar_chart(df)
    # df.plot(kind='bar')
    # plt.show()  

##### Code by Jav  #####
##### Code by Shing  #####
def shing2(df):
    #df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
    #df = pd.read_csv(r"C:\users\shing\Desktop\INF1002 Project\mergedDatafilter.csv")
    df = df.dropna()
    df = df.drop(columns=['event_type'])
    df = df.drop(columns=['category_code'])
    df = df.drop(columns=['brand'])
    df['event_time'] = (df['event_time'].str[:10])

    df = df.groupby([df.event_time])["price"].sum()
    #st.bar_chart(df.event_time.dt.date.unique(),dfByDate)
    st.bar_chart(df)
##### Code by Shing  #####


