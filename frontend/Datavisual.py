from chart import chart1,chart2,chart3
import streamlit as st

def chartframe():
    col1, col2= st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.header("chart 1")      
        chart3()

    with col2:
        option = st.selectbox('Please select the month you want to view',('Jan 2020', 'Oct 2019'))
        if option == "Jan 2020":
            st.header("Number of Daily sale of January 2020")
            chart2()
        elif option == "Oct 2019":
            st.header("Number of Daily sale of October 2019")
            chart3()

    with col3:
        st.header("chart 3")
        chart3()
        
    with col4:
        st.header("chart 4")
        
        