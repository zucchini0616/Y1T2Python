# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from collections import OrderedDict
import streamlit as st
# Reading local CSV file and assigning them to a list

def calvin1(df):
    brand_name = df[df.columns[3]].tolist()

    # Putting Brand: Quantity into dictionary sorted from highest to lowest
    brand_counter = dict(Counter(brand_name))
    x = OrderedDict(sorted(brand_counter.items(), reverse = True, key=lambda t: t[1]))

    # Retrieving top 5 brands with the highest quantities from the dictionary
    n = 5
    topNBrands = dict(list(x.items())[0: n])

    # Data to plot
    labels = []
    sizes = []

    for x, y in topNBrands.items():
        labels.append(x)
        sizes.append(y)

    # Plot
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%')

    ax1.axis('equal')




    st.pyplot(fig1)
