import streamlit as st
from OctCategory import category,shing1,jav1
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
        'Dec 2019', 'Nov 2019', 'Oct 2019'))
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
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
                calvin2(df)
            with col5:
                st.header("No. of purchase trend in April")
                chart2(db)
            with col6:
                st.header("Sales amount over from Oct 2019 to Apr 2020")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))   
                shing1(df)

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
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
                calvin2(df)
            with col5:
                st.header("No. of purchase trend in March")
                chart2(db)
            with col6:
                st.header("Sales amount over from Oct 2019 to March 2020")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))   
                shing1(df)


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
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
                calvin2(df)
            with col5:
                st.header("No. of purchase trend in Feburary")
                chart2(db)
            with col6:
                st.header("Sales amount over from Oct 2019 to Apr 2020")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))   
                shing1(df)

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
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
                calvin2(df)
            with col5:
                st.header("No. of purchase trend in January")
                chart2(db)
            with col6:
                st.header("Sales amount over from Oct 2019 to Apr 2020")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))   
                shing1(df)

    elif option == "Dec 2019":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\Dec20.csv")
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
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
                calvin2(df)
            with col5:
                st.header("No. of purchase trend in December")
                chart2(db)
            with col6:
                st.header("Sales amount over from Oct 2019 to Apr 2020")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))   
                shing1(df)

    elif option == "Nov 2019":
            col1, col2= st.columns(2)
            col3, col4= st.columns(2)
            col5, col6= st.columns(2)
            db = pd.read_csv("data\Nov20.csv")
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
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
                calvin2(df)
            with col5:
                st.header("No. of purchase trend in November")
                chart2(db)
            with col6:
                st.header("Sales amount over from Oct 2019 to Apr 2020")
                df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))   
                shing1(df)

    elif option == "Oct 2019":
        col1, col2= st.columns(2)
        col3, col4= st.columns(2)
        col5, col6= st.columns(2)
        db = pd.read_csv("data\Oct20.csv")
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
            df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
            calvin2(df)
        with col5:
            st.header("No. of purchase trend in October")
            chart2(db)
        with col6:
            st.header("Sales amount over from Oct 2019 to Apr 2020")
            df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))   
            shing1(df)
        