#from st_on_hover_tabs import on_hover_tabs
from re import M
import streamlit as st
import pandas as pd
import time
import numpy as np
from math import ceil

#C:\Users\Admin\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\streamlit
#change server.maxMessageSize

#N = 10
def viewing():

  apr20_df = pd.read_csv("data/Apr20.csv")
  mar20_df = pd.read_csv("data/Mar20.csv")
  feb20_df = pd.read_csv("data/Feb20.csv")
  jan20_df = pd.read_csv("data/Jan20.csv")
  dec19_df = pd.read_csv("data/Dec19.csv")
  nov19_df = pd.read_csv("data/Nov19.csv")
  oct19_df = pd.read_csv("data/Oct19.csv")

  result = pd.concat([apr20_df,mar20_df,feb20_df,jan20_df,dec19_df,nov19_df,oct19_df])

  cd = "data"
  st.markdown("# Data Viewing")

  data = result
  df6 = data.copy()
  filter1,filter2,export= st.columns(3)
  with filter1:
    options_brand = data['brand'].unique().tolist()
    selected_brand = st.multiselect('Search By brand',options_brand)
  with filter2:
    options_mth = data['event_time'].str[:7].unique().tolist()
    selected_mth = st.multiselect('Search By month',options_mth)
  def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

  with export:
    st.write("")
    st.download_button(     
      label="Download as CSV",
      data=convert_df_to_csv(df6),
      file_name='download.csv',
      mime='text/csv',
    )
  if selected_brand:
      df6 = df6[df6["brand"].isin(selected_brand)]

  if selected_mth:
      df6 = df6[df6['event_time'].str[:7].isin(selected_mth)]


  if selected_brand or selected_mth:
      st.dataframe(df6.reset_index(drop = True))
      cd = "df6"
  else:
      st.dataframe(data)


def viewing1(pd):



  


  st.markdown("# Data Viewing")

  data = pd
  df6 = data.copy()
  filter1,export= st.columns(2)
  with filter1:
    options_brand = data['brand'].unique().tolist()
    selected_brand = st.multiselect('Search By brand',options_brand)
 
  def convert_df_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

  with export:
    st.write(" ")
    st.download_button(     
      label="Download as CSV",
      data=convert_df_to_csv(df6),
      file_name='download.csv',
      mime='text/csv',
    )
  if selected_brand:
      df6 = df6[df6["brand"].isin(selected_brand)]




  if selected_brand:
      st.dataframe(df6.reset_index(drop = True))
      cd = "df6"
  else:
      st.dataframe(data)


  ###################download#####################

  #st.dataframe(data)


