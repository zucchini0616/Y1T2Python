
import csv
import pandas as pd
import os
import glob



# read the top n rows of csv file as a dataframe
oct2019_df = pd.read_csv("2019-Oct.csv", nrows=100000)
nov2019_df = pd.read_csv("2019-Nov.csv", nrows=100000)
dec2019_df = pd.read_csv("2019-Dec.csv", nrows=100000)
jan2020_df = pd.read_csv("2020-Jan.csv", nrows=100000)
feb2020_df = pd.read_csv("2020-Feb.csv", nrows=100000)
mar2020_df = pd.read_csv("2020-Mar.csv", nrows=100000)
apr2020_df = pd.read_csv("2020-Apr.csv", nrows=100000)

#filtering event_type to only purchase
dfOct = oct2019_df.query("event_type == 'purchase'")
dfNov = nov2019_df.query("event_type == 'purchase'")
dfDec = dec2019_df.query("event_type == 'purchase'")
dfJan = jan2020_df.query("event_type == 'purchase'")
dfFeb = feb2020_df.query("event_type == 'purchase'")
dfMar = mar2020_df.query("event_type == 'purchase'")
dfApr = apr2020_df.query("event_type == 'purchase'")


# print the shape of the dataframe

    
os.chdir("/Users/Bin/Desktop/VS Code/python3")


#export to csv
frames = [dfOct, dfNov,dfDec,dfJan, dfFeb, dfMar, dfApr]
result = pd.concat(frames)
result.to_csv( "mergedData.csv", index=False, encoding='utf-8-sig')

