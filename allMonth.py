
import csv
import pandas as pd
import os
import glob
import matplotlib.pyplot as plt


# read the top n rows of csv file as a dataframe
oct2019_df = pd.read_csv("Oct19.csv")
nov2019_df = pd.read_csv("Nov19.csv")
dec2019_df = pd.read_csv("Dec19.csv")
jan2020_df = pd.read_csv("Jan20.csv")
feb2020_df = pd.read_csv("Feb20.csv")
mar2020_df = pd.read_csv("Mar20.csv")
apr2020_df = pd.read_csv("Apr20.csv")



# #filtering event_type to only purchase



# print the shape of the dataframe

    
os.chdir("/Users/Bin/Desktop/VS Code/python3/Project")



#Cleaning Category Column
oct2019_df['category_code'] = oct2019_df['category_code'].str.split('.').str[0]
nov2019_df['category_code'] = nov2019_df['category_code'].str.split('.').str[0]
dec2019_df['category_code'] = dec2019_df['category_code'].str.split('.').str[0]
jan2020_df['category_code'] = jan2020_df['category_code'].str.split('.').str[0]
feb2020_df['category_code'] = feb2020_df['category_code'].str.split('.').str[0]
mar2020_df['category_code'] = mar2020_df['category_code'].str.split('.').str[0]
apr2020_df['category_code'] = apr2020_df['category_code'].str.split('.').str[0]
#testdf['category_code'] = testdf['category_code'].str.split('.').str[0]


#merging all month together
frames = [oct2019_df, nov2019_df,dec2019_df,jan2020_df, feb2020_df, mar2020_df, apr2020_df]
result = pd.concat(frames)
#result.drop('event_type', inplace=True, axis=1)

result['event_time'] = pd.to_datetime(result['event_time'])
#testdf['event_time'] = pd.to_datetime(testdf['event_time'])

#sorting by date
#result = result.sort_values(by="event_time")
#result = result["event_time"].dt.strftime("%yyyy%mm")

#result['event_time'].dt.to_period('M')
#result['event_time'] = result['event_time'].dt.year
year = result.groupby(result.event_time.dt.year)['category_code'].value_counts()
month = result.groupby(result.event_time.dt.month)['category_code'].value_counts()
#monthTest = testdf.groupby(testdf.event_time.dt.month)['category_code'].value_counts()



#result['event_time'].value_counts().nlargest(5).plot(kind='bar')
#print(result.head())
#plt.show()
#print(result.head())
#result.to_csv( "mergedAllMonth.csv", index=False, encoding='utf-8-sig')