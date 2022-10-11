import csv
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt
import numpy as np

db = pd.read_csv('Oct19.csv')

df = pd.DataFrame(db)

cat = df['category_code']
accessories = cat.str.contains('accessories')
apparel = cat.str.contains('apparel')

#df['category_code'] = np.where(accessories, 'accessories',
         #                             np.where(apparel, 'apparel',
                       #                        cat.str.replace('.', ' ')))
                                               
#df['category_code'].value_counts()[-1:-5].plot(kind='bar')
df['category_code'] = df['category_code'].str.split('.').str[0]
df['category_code'].value_counts().nlargest(5).plot(kind='bar')

plt.title("Top 5 category of October 2019")
plt.xlabel("Category")
plt.ylabel("Number of purchases")
plt.show()

#print(a)
#plt.hist(a)
#plt.show()
