import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Oct19.csv')

df['category_code'] = df['category_code'].astype('string')
df['category_code'] = df['category_code'].str.split(".", expand=True)[0]
df.groupby('category_code')['price'].agg(['sum']).sort_values('sum', ascending= False)[:5].plot(kind='bar')
plt.show()