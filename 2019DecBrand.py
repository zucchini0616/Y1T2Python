import csv
import pandas as pd
import os
import glob

import matplotlib.pyplot as plt

db = pd.read_csv('Oct19.csv')

db = db.dropna()

db.sort_values(["brand"],
					axis=0,
					ascending=[True],
					inplace=True)

db = db.query("event_type == 'purchase'")

#to_drop = ['event_type','event_time', 'category_code', 'price']
#db.drop(to_drop, inplace=True, axis=1)

df = pd.DataFrame(db)


df['brand'].value_counts()[:5].plot(kind='pie')

plt.title("Top 5 Brand in 2019 October")
plt.legend()

plt.show()
#print(countX(brandList, 'apple'))

#df.drop(df[df['brand'].value_counts() == 1].index, inplace = True)
#test = df.loc[df.brand == 1]

#test = df.loc[df.brand.value_counts() != 1]

#print(apple)


# for row in df:
# 	x = df.row['brand'].value_counts() != 1
# 	if x == False:
# 		df.drop(df(x))







#plt.hist(df.brand.value_counts() != 1)

#print(df['brand'].value_counts())
    


        




