import streamlit as st
import time
import numpy as np
import pandas as pd
from dailysales import dailysalesjan,dailysalesOct
from OctCategory import category

# def chart1():
#     db = pd.read_csv("data\Oct19.csv")
#     category(db)

def chart2():
    data = dailysalesjan()    
    st.line_chart(data)
def chart3():
    data = dailysalesOct()    
    st.line_chart(data)


