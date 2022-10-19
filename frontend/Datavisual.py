import streamlit as st
from OctCategory import category,shing1,shing2,jav1
import pandas as pd
import  glob
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from collections import OrderedDict
from TopFiveBrands_Month import   calvin1
from PriceCategorization import calvin2
from chart import  chart2
def chartframe():
    option = st.selectbox('Please select the month you want to view',('Apr 2020', 'Mar 2020', 'Feb 2020', 'Jan 2020',
        'Dec 2019', 'Nov 2019', 'Oct 2019', 'All available months'))
    if option == "Apr 2020":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\Apr20.csv")
            with col1:
                st.header("Top 5 category of April 2020 by no. of purchase")             
                category(db)
            with col2:
                st.header("Top 5 category of April 2020 by sales amount")
                jav1(db)
            with col3:
                st.header("Top 5 brand of April 2020 by no. of purchase")
                calvin1(db)
            with col4:
                st.header("Price Range of April")
                
                calvin2(db)
            with col5:
                st.header("No. of purchase trend in April")
                chart2(db)
            with col6:
                st.header("Sales amount per day in April")
                   
                shing2(db)

    elif option == "Mar 2020":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\Mar20.csv")
            with col1:
                st.header("Top 5 category of March 2020 by no. of purchase")             
                category(db)
            with col2:
                st.header("Top 5 category of March 2020 by sales amount")
                jav1(db)
            with col3:
                st.header("Top 5 brand of March 2020 by no. of purchase")
                calvin1(db)
            with col4:
                st.header("Price Range of March")
                
                calvin2(db)
            with col5:
                st.header("No. of purchase trend in March")
                chart2(db)
            with col6:
                st.header("Sales amount over per day in March")
                   
                shing2(db)


    elif option == "Feb 2020":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\Feb20.csv")
            with col1:
                st.header("Top 5 category of Feburary 2020 by no. of purchase")             
                category(db)
            with col2:
                st.header("Top 5 category of Feburary 2020 by sales amount")
                jav1(db)
            with col3:
                st.header("Top 5 brand of Feburary 2020 by no. of purchase")
                calvin1(db)
            with col4:
                st.header("Price Range of Feburary")
                
                calvin2(db)
            with col5:
                st.header("No. of purchase trend in Feburary")
                chart2(db)
            with col6:
                st.header("Sales amount per day in February")
                   
                shing2(db)

    elif option == "Jan 2020":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\Jan20.csv")
            with col1:
                st.header("Top 5 category of January 2020 by no. of purchase")             
                category(db)
            with col2:
                st.header("Top 5 category of January 2020 by sales amount")
                jav1(db)
            with col3:
                st.header("Top 5 brand of January 2020 by no. of purchase")
                calvin1(db)
            with col4:
                st.header("Price Range of January")
                
                calvin2(db)
            with col5:
                st.header("No. of purchase trend in January")
                chart2(db)
            with col6:
                st.header("Sales amount per day in January")
                   
                shing1(db)

    elif option == "Dec 2019":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\Dec19.csv")
            with col1:
                st.header("Top 5 category of December 2020 by no. of purchase")             
                category(db)
            with col2:
                st.header("Top 5 category of December 2020 by sales amount")
                jav1(db)
            with col3:
                st.header("Top 5 brand of December 2020 by no. of purchase")
                calvin1(db)
            with col4:
                st.header("Price Range of December")
                #
                calvin2(db)
            with col5:
                st.header("No. of purchase trend in December")
                chart2(db)
            with col6:
                st.header("Sales amount per day in December")
                   
                shing2(db)

    elif option == "Nov 2019":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\\Nov19.csv")
            with col1:
                st.header("Top 5 category of November 2020 by no. of purchase")             
                category(db)
            with col2:
                st.header("Top 5 category of November 2020 by sales amount")
                jav1(db)
            with col3:
                st.header("Top 5 brand of November 2020 by no. of purchase")
                calvin1(db)
            with col4:
                st.header("Price Range of November")
                
                calvin2(db)
            with col5:
                st.header("No. of purchase trend in November")
                chart2(db)
            with col6:
                st.header("Sales amount per day in November")
                   
                shing2(db)

    elif option == "Oct 2019":
        col1, col2= st.columns(2)
        col3, col4= st.columns(2)
        col5, col6= st.columns(2)
        db = pd.read_csv("data\Oct19.csv")
        with col1:
            st.header("Top 5 category of October 2020 by no. of purchase")             
            category(db)
        with col2:
            st.header("Top 5 category of October 2020 by sales amount")
            jav1(db)
        with col3:
            st.header("Top 5 brand of October 2020 by no. of purchase")
            calvin1(db)
        with col4:
            st.header("Price Range of October")
            
            calvin2(db)
        with col5:
            st.header("No. of purchase trend in October")
            chart2(db)
        with col6:
            st.header("Sales amount per day in October")
               
            shing1(db)
        
    elif option == "All available months":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
            with col1:
                st.header("Top 5 category of all months by no. of purchase")             
                category(db)
            with col2:
                st.header("Top 5 category of all months by sales amount")
                jav1(db)
            with col3:
                st.header("Top 5 brand of all months by no. of purchase")
                calvin1(db)
            with col4:
                st.header("Price Range of all months")
                
                calvin2(db)
            with col5:
                st.header("No. of purchase trend for all months")
                chart2(db)
            with col6:
                st.header("Sales amount over all months")
                   
                shing1(db)        