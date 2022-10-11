from chart import chart1,chart2,chart3
import streamlit as st
from OctCategory import category
import pandas as pd
def chartframe():
    option = st.selectbox('Please select the month you want to view',('Apr 2020', 'Mar 2020', 'Feb 2020', 'Jan 2020',
        'Dec 2019', 'Nov 2019', 'Oct 2019'))
    if option == "Jan 2020":
            col1, col2= st.columns(2)
            with col1:
                st.header("Number of Daily sale of January 2020")
                chart2()
            with col2:
                st.header("Top 5 category of January 2020")
                db = pd.read_csv("data\Jan20.csv")               
                category(db)
    elif option == "Oct 2019":
            col1, col2= st.columns(2)
            with col1:
                st.header("Number of Daily sale of October 2019")
                chart3()
            with col2:
                st.header("Top 5 category of October 2019")
                db = pd.read_csv("data\Oct19.csv")              
                category(db)
                
        # col1, col2= st.columns(2)
        # # col3, col4 = st.columns(2)

        # with col1:    
        #         chart1()

        # with col2:


    # with col3:
    #     st.header("chart 3")
    #     chart3()
        
    # with col4:
    #     st.header("chart 4")
        
        