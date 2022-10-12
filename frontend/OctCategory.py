import csv
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st



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

def shing(db):
    df = pd.concat(map(pd.read_csv, glob.glob(r'C:\Users\shing\Desktop\INF1002 Project\Data/*.csv')))
    # df = pd.read_csv(r"C:\users\shing\Desktop\INF1002 Project\mergedDatafilter.csv")
    df = df.dropna()
    df = df.drop(columns=['event_type'])
    df = df.drop(columns=['category_code'])
    df = df.drop(columns=['brand'])
    df['event_time'] = pd.to_datetime(df['event_time'])

    dfByMonth = df.groupby([df.event_time.dt.year,df.event_time.dt.month])["price"].sum()
    plt.bar(df.event_time.dt.to_period('M').dt.strftime('%m/%Y').unique(),dfByMonth)
    plt.show()

# .plot(kind='bar')
    # plt.title("Top 5 category of October 2019")
    # plt.xlabel("Category")
    # plt.ylabel("Number of purchases")
    # plt.show()

#print(a)
#plt.hist(a)
#plt.show()
# category(db)