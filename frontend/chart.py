import streamlit as st
import time
import numpy as np
import pandas as pd
from dailysales import dailysalesjan,dailysalesOct
from OctCategory import category

def chart1():
    category()
    # progress_bar = st.sidebar.progress(0)
    # status_text = st.sidebar.empty()
    # last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    # for i in range(1, 50):
    #     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    #     status_text.text("%i%% Complete" % i)
    #     chart.add_rows(new_rows)
    #     progress_bar.progress(i)
    #     last_rows = new_rows
    #     time.sleep(0.05)

    # progress_bar.empty()

def chart2():
    data = dailysalesjan()    
    st.line_chart(data)
def chart3():
    data = dailysalesOct()    
    st.line_chart(data)


