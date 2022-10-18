from chart import chart2,chart3
import streamlit as st
from OctCategory import category,shing1,shing2
import pandas as pd
import  glob
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from collections import OrderedDict
from TopFiveBrands_Month import   calvin1
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
            col3, col4= st.columns(2)
            col5, col6 = st.columns(2)
            with col1:
                st.header("Number of Daily sale of October 2019")
                chart3()
            with col2:
                st.header("Top 5 category of October 2019")
                db = pd.read_csv("data/Oct19.csv")         
                #df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))     
                category(db)
            with col3:
                st.header("Sales amount from Oct 19 to Apr 20")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
            #db = pd.read_csv("data\Oct19.csv")              
                shing1(df)
            with col4:
                st.header("Top 5 category of October 2019 per day")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
                shing2(df)
            with col5:
                st.header("Top 5 category of October 2019 per day")

    elif option == "Nov 2019":
            
            st.header("Sales amount from Oct 19 to Apr 20")
            df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
            #db = pd.read_csv("data\Oct19.csv")              
            shing1(df)

    elif option == "Feb 2020":
            col1, col2= st.columns(2)
            with col1:
                st.header("Sales amount from Oct 19 to Apr 20")
                df = pd.read_csv('data/Feb20.csv')
                # db = pd.read_csv("data\Oct19.csv")              
                calvin1(df)
            with col2:
                st.header("Sales amount from Oct 19 to Apr 20")
                df = pd.read_csv('data/Mar20.csv')
                # db = pd.read_csv("data\Oct19.csv")              
                calvin1(df)
          
            
                # db = pd.read_csv("data\Oct19.csv")              
                # shing2(db)
                
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
        
        