from email.mime import image
from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import pandas as pd
import time
import numpy as np
from view import viewing,viewing1
from Datavisual import chartframe
from PIL import Image
from io import StringIO
from OctCategory import category,shing1,jav1
from TopFiveBrands_Month import   calvin1
from PriceCategorization import calvin2
from chart import  chart2

st.set_page_config(layout="wide")

# my_dataframe = pd.read_csv('sample.csv')

# st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Data Viewing', 'Data Visualisation','Insights','User Input'], 
                             iconName=['-', '-', '-','-'],
                             styles = {'navtab': {'background-color':'#111',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                       'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},
                                       'iconStyle':{'position':'fixed',
                                                    'left':'7.5px',
                                                    'text-align': 'left'},
                                       'tabStyle' : {'list-style-type': 'none',
                                                     'margin-bottom': '30px',
                                                     'padding-left': '30px'}}, default_choice=0)

if tabs =='Data Viewing':
    # st.dataframe(my_dataframe)
    st.title("Data Visualisation")
    viewing()
elif tabs == 'Data Visualisation':
    st.title("Data Visualisation")

    chartframe()
elif tabs == 'Insights':
    st.title("Insights")
    col1, col2= st.columns(2)
    col3, col4= st.columns(2)
    col5, col6= st.columns(2)
    col7, col8= st.columns(2)
    with col1:
        st.header("Total sale price of all months")
        image = Image.open('img/sales.png')
        st.image(image, caption='Sale price of all months')
    with col2:
        st.header("Analysis")
        st.markdown("To get average total sales per Month/Day, we must first get the datetime from the database using pandas.to datetime(), then group it by Month/Date and then get the total sales from it using .sum()\n\n" + 
        "The graphs shows that the highest total sales recorded during the month of October - December 2019 pre-covid was at $3.254871e+08 in December 2019 and $2.415604e+08 in November. And, from January to April 2020 during covid, the highest total sales recording was $3.604690e+08 in February 2020 and $2.982014e+08 in March 2020, on a more even daily total sale.\n\n" +
        "We can see that as the covid pandemic becomes more serious, total sales increase. February 2020, December 2019 and March 2020 were the top three months for total sales. While looking at the total sales for the days prior to covid, we can see that the daily sales are very low compared to the daily sales during covid, with the exception of one or two days in December that have the highest daily sales recorded.\n\n" +
        "We can assume that everyone was shopping and planning for the year's final major event, Christmas, in December 2019. Covid cases rise globally in February 2020, as China enters a state of emergency. In March 2020, over 100 countries worldwide went into lockdown, forcing everyone to stay at home. Since most people were at home, we could conclude that the way to purchase items or necessities was through E-commerce business. So, if we compare Total Sales in November (Pre-Covid and No Major Event happening) to Total Sales in February (During-Covid and No Major Event happening), we see a 49.2252% increase.")
    with col3:
        st.header("Analysis")
        st.markdown("To get average total sales per Month/Day, we must first get the datetime from the database using pandas.to datetime(), then group it by Month/Date and then get the total sales from it using .sum()\n\n" + 
        "The graphs shows that the highest total sales recorded during the month of October - December 2019 pre-covid was at $3.254871e+08 in December 2019 and $2.415604e+08 in November. And, from January to April 2020 during covid, the highest total sales recording was $3.604690e+08 in February 2020 and $2.982014e+08 in March 2020, on a more even daily total sale.\n\n" +
        "We can see that as the covid pandemic becomes more serious, total sales increase. February 2020, December 2019 and March 2020 were the top three months for total sales. While looking at the total sales for the days prior to covid, we can see that the daily sales are very low compared to the daily sales during covid, with the exception of one or two days in December that have the highest daily sales recorded.\n\n" +
        "We can assume that everyone was shopping and planning for the year's final major event, Christmas, in December 2019. Covid cases rise globally in February 2020, as China enters a state of emergency. In March 2020, over 100 countries worldwide went into lockdown, forcing everyone to stay at home. Since most people were at home, we could conclude that the way to purchase items or necessities was through E-commerce business. So, if we compare Total Sales in November (Pre-Covid and No Major Event happening) to Total Sales in February (During-Covid and No Major Event happening), we see a 49.2252% increase.")
    with col4:
        st.header("Total number of sales of all months")
        image = Image.open('img/price.png')
        st.image(image, caption='Sales of all months')
    with col5:
        st.header("Top 5 category sales of all months")
        image = Image.open('img/categotyAllMonth.png')
        st.image(image, caption='Top 5 category sales of all months')
    with col6:
        st.header("Analysis")
        st.markdown("From the graph, we can see that during October - December 2019 pre-covid. Electronics is the most popular category with 995609 purchases. And from January - April 2020, we can see that Home appliances and construction items and tools for houses are the most popular category and in general, the number of purchases made have also increased by 42% from pre-covid to covid period.\n\n" + 
        "Based on the graph, we can see that as when Covid gets more widespread and people are forced to stay home, the more people start to buy things online with a 42% increase in total purchases. And the items that people choose to buy also changes from electronics to household items.\n\n" +
        "Entrepreneurs that want to start an ecommerce business now should focus on categories like Appliances and household items to make the most profit. It is also a good time to start an ecommerce business as online shopping is getting more popular.Based on the graph, manufacturers should produce more products in these categories in order to meet the demand.\n\n")    
    with col7:
        st.header("Analysis")
        st.markdown("From the graph, we can tell that Electronics has the most amount of sales compared to other categories and the difference between the total sales for Electronics is very huge compared to the 2nd place category, Appliances. Total sales amount for Electronics in the month of October 2019 itself is at $175 million while the total sales amount for Appliances is $15 million.\n\n")
    with col8:
        st.header("Total 5 category price of all months")
        image = Image.open('img/price.png')
        st.image(image, caption='Sales of all months')

elif tabs == 'User Input':
    st.title("User Input")
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        # bytes_data = uploaded_file.getvalue()
        # st.write(bytes_data)

        # To convert to a string based IO:
        # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # st.write(stringio)

        # To read file as string:
        # string_data = stringio.read()
        # st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        viewing1(dataframe)
        # st.write(dataframe)
        
        col1, col2= st.columns(2)
        col3, col4= st.columns(2)
        col5, col6= st.columns(2)
        
        with col1:
            st.header("Top 5 category  by no. of purchase")             
            category(dataframe)
        with col2:
            st.header("Top 5 category  by sales amount")
            jav1(dataframe)
        with col3:
            st.header("Top 5 brand  by no. of purchase")
            calvin1(dataframe)
        with col4:
            st.header("Price Range ")
            calvin2(dataframe)
        with col5:
            st.header("No. of purchase trend ")
            chart2(dataframe)

