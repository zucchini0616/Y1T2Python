from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import pandas as pd
import time
import numpy as np
from Datavisual import chartframe
st.set_page_config(layout="wide")

my_dataframe = pd.read_csv('mergedData.csv')

# st.header("Custom tab component for on-hover navigation bar")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Data Viewing', 'Data Visualisation', 'Data Information','Insights'], 
                             iconName=['Data Viewing', 'Data Visualisation', 'Data Information','Insights'],
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
    st.title("Data Viewing")
    st.write('Name of option is {}'.format(tabs))
    st.dataframe(my_dataframe)
    


elif tabs == 'Data Visualisation':
    st.title("Data Visualisation")
    st.write('Name of option is {}'.format(tabs))
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

elif tabs == 'Data Information':
    st.title("Data Information")
    st.write('Name of option is {}'.format(tabs))

elif tabs == 'Insights':
    st.title("Insights")
    st.write('Name of option is {}'.format(tabs))
    
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