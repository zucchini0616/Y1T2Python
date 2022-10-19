import streamlit as st
import time
import numpy as np
import pandas as pd
# def chart1():
#     db = pd.read_csv("data\Oct19.csv")
#     category(db)

def chart2(df):

    
    df['event_time'] = df['event_time'].astype('string')
    
    df['event_time'] = df['event_time'].str.split(r" ", expand=True)[0]
    df = df['event_time'].value_counts()
       
    st.line_chart(df)



