from email.mime import image
from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import pandas as pd
import time
import numpy as np
from view import viewing    
from Datavisual import chartframe
from PIL import Image

st.set_page_config(layout="wide")

# my_dataframe = pd.read_csv('sample.csv')

# st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Data Viewing', 'Data Visualisation','Insights'], 
                             iconName=['-', '-', '-'],
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
    viewing()



elif tabs == 'Data Visualisation':
    st.title("Data Visualisation")

    chartframe()
    # progress_bar = st.sidebar.progress(0)
    # status_text = st.sidebar.empty()
    # last_rows = np.random.randn(1, 1)
    # chart = st.line_chart(last_rows)

    # for i in range(1, 100):
    #     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    #     status_text.text("%i%% Complete" % i)
    #     chart.add_rows(new_rows)
    #     progress_bar.progress(i)
    #     last_rows = new_rows
    #     time.sleep(0.05)

    # progress_bar.empty()

    # # Streamlit widgets automatically run the script from top to bottom. Since
    # # this button is not connected to any other logic, it just causes a plain
    # # rerun.
    # st.button("Re-run")


elif tabs == 'Insights':
    st.title("Insights")
    col1, col2= st.columns(2)
    col3, col4= st.columns(2)
    col5, col6= st.columns(2)
    col7, col8= st.columns(2)
    col9, col10= st.columns(2)
    col11, col12= st.columns(2)
    col13, col14= st.columns(2)


    with col1:
        st.header("Total sale price of all months")
        image = Image.open('img/sales.png')
        st.image(image, caption='Sale price of all months')
    with col2:
        st.header("Analysis")
        st.markdown("To get average total sales per Month/Day, we must first get the datetime from the database using pandas.to datetime(), then group it by Month/Date and then get the total sales from it using .sum()\n\n" + 
        "The graphs shows that the highest total sales recorded during the month of October - December 2019 pre-covid was at \\$3.254871e+08 in December 2019 and \\$2.415604e+08 in November. And, from January to April 2020 during covid, the highest total sales recording was \\$3.604690e+08 in February 2020 and \\$2.982014e+08 in March 2020, on a more even daily total sale.\n\n" +
        "We can see that as the covid pandemic becomes more serious, total sales increase. February 2020, December 2019 and March 2020 were the top three months for total sales. While looking at the total sales for the days prior to covid, we can see that the daily sales are very low compared to the daily sales during covid, with the exception of one or two days in December that have the highest daily sales recorded.\n\n" +
        "We can assume that everyone was shopping and planning for the year's final major event, Christmas, in December 2019. Covid cases rise globally in February 2020, as China enters a state of emergency. In March 2020, over 100 countries worldwide went into lockdown, forcing everyone to stay at home. Since most people were at home, we could conclude that the way to purchase items or necessities was through E-commerce business. So, if we compare Total Sales in November (Pre-Covid and No Major Event happening) to Total Sales in February (During-Covid and No Major Event happening), we see a 49.2252% increase.")
    with col3:
        st.header("Analysis")
        st.markdown("To get average total sales per Month/Day, we must first get the datetime from the database using pandas.to datetime(), then group it by Month/Date and then get the total sales from it using .sum()\n\n" + 
        "The graphs shows that the highest total sales recorded during the month of October - December 2019 pre-covid was at \\$3.254871e+08 in December 2019 and \\$2.415604e+08 in November. And, from January to April 2020 during covid, the highest total sales recording was \\$3.604690e+08 in February 2020 and \\$2.982014e+08 in March 2020, on a more even daily total sale.\n\n" +
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
        st.markdown("From the graph, we can tell that Electronics has the most amount of sales compared to other categories and the difference between the total sales for Electronics is very huge compared to the 2nd place category, Appliances. Total sales amount for Electronics in the month of October 2019 itself is at \\$175 million while the total sales amount for Appliances is \\$15 million.\n\n")
    with col8:
        st.header("Total 5 category price of all months")
        image = Image.open('img/price.png')
        st.image(image, caption='Sales of all months')
    with col9:
        st.header("Top 5 brand of all months")
        image = Image.open('img/piee.png')
        st.image(image, caption='Top 5 brand of all months')
    with col10:
        st.header("Analysis")
        st.markdown("From the graph, there is an obvious trend that the top 5 companies by sales made were almost exclusively tech giants such as Samsung, Apple, Xiaomi, Huawei and Oppo. Across all months, Samsung leads the market share of the top 5 brands ranging from 38.2% to 50.5% of sales made. They are followed closely by Apple with an average market share of 33.5%. Xiaomi then follows behind with about 12-15% and finally Huawei and Oppo close out the top 5 brands with about 6% and 4.5 % respectively.\n\n" + 
        "Based on the graph, we can conclude that tech giants cement their place as major companies with extremely large revenue and sales despite the immersion of the Covid-19 pandemic. This is useful to investors and manufacturers to ensure that tech companies will not be going anywhere and will not be overtaken by other industries even in pandemic times.")
    with col11:
        st.header("Analysis")
        st.markdown("From the graph, the trend of sales are generally consistent across all price ranges over all the months. Purchases are mainly dominated by items costing between \\$100 - \\$250. All purchase categories less than \\$2000 follow the trend of peaking on December 2019, likely due to increased shopping during Christmas, followed by an average month of January, and then another peak on February 2020 at the height of the Covid-19 pandemic, where number of sales matched and even exceeded that of December 2019.  Purchases above \\$2000 did not follow the trend of two peak periods, but steadily increased month by month until its peak February 2020. While most price categories start to decline after their peak in February 2020, purchases costing \\$250 - \\$ 500 remained at near peak levels all through to at least April 2020. Purchases costing less than \\$50 also remained near peak, and even set a new high on April 2020.\n\n"
        +"Based on the graph, we can conclude that people are less likely to purchase expensive items after the immersion of the Covid-19 pandemic, and are mostly buying cheaper items such as household necessities. This benefits smaller industries who are able to create cheaper new products or seize new markets, while companies such as phone makers and tech giants lose out have a slower fiscal year.")
    with col12:
        st.header("Price Range of all months")
        image = Image.open('img/range.png')
        st.image(image, caption='Price Range of all months')
    with col13:
        st.header("Top 5 category of all months by sales amount")
        image = Image.open('img/salesAmt.png')
        st.image(image, caption='Top 5 category of all months by sales amount')
    with col14:
        st.header("Analysis")
        st.markdown("From the graph, we can tell that Electronics has the most amount of sales compared to other categories and the difference between the total sales for Electronics is very huge compared to the 2nd place category, Appliances. Total sales amount for Electronics in the month of October 2019 itself is at \\$175 million while the total sales amount for Appliances is \\$15 million.\n\n" + 
        "Based on the graph, entrepreneurs that want to go into the eCommerce sector can look to market Electronic products or Appliances in order to make the most sales and manufacturers can look to produce more of these Electronics products in order to meet the huge market demand.")
# To implement with styles:

# (These are the current default CSS styles for the tabs)

# with st.sidebar:
#         tabs = on_hover_tabs(tabName=['Data Viewing', 'Data Visualisation', 'Data Information','Insights'], 
#                              iconName=['Data Viewing', 'Data Visualisation', 'Data Information','Insights'],
#                              styles = {'navtab': {'background-color':'#111',
#                                                   'color': '#818181',
#                                                   'font-size': '18px',
#                                                   'transition': '.3s',
#                                                   'white-space': 'nowrap',
#                                                   'text-transform': 'uppercase'},
#                                        'tabOptionsStyle': {':hover :hover': {'color': 'red',
#                                                                       'cursor': 'pointer'}},
#                                        'iconStyle':{'position':'fixed',
#                                                     'left':'7.5px',
#                                                     'text-align': 'left'},
#                                        'tabStyle' : {'list-style-type': 'none',
#                                                      'margin-bottom': '30px',
#                                                      'padding-left': '30px'}},
#                              key="1")