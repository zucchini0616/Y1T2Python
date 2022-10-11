import pandas as pd
import glob 
import matplotlib.pyplot as plt

df = pd.concat(map(pd.read_csv, glob.glob(r'C:\Users\shing\Desktop\INF1002 Project\Data/*.csv')))
# df = pd.read_csv(r"C:\users\shing\Desktop\INF1002 Project\mergedDatafilter.csv")
df = df.dropna()
df = df.drop(columns=['event_type'])
df = df.drop(columns=['category_code'])
df = df.drop(columns=['brand'])
df['event_time'] = pd.to_datetime(df['event_time'])

dfByDate = df.groupby([df.event_time.dt.year,df.event_time.dt.month])["price"].sum()
plt.bar(df.event_time.dt.date.unique(),dfByDate)
plt.show()

#if inputA[0] == 'year':
#    dfByTotalyear = df.groupby(df.event_time.dt.year)["price"].max()
#    print(df.event_time.dt.year.unique())
#    plt.bar(df.event_time.dt.strftime('%Y').unique(),dfByTotalyear)
#    plt.show()
#elif inputA[0] == 'month':
#    dfByMonth = df.groupby([df.event_time.dt.year,df.event_time.dt.month])["price"].max()
#    print(dfByMonth)
#    plt.bar(df.event_time.dt.to_period('M').dt.strftime('%m/%Y').unique(),dfByMonth)
#    plt.show()
#elif inputA[0] == 'date':
#    dfByDate = df.groupby([df.event_time.dt.date])["price"].max()
#    print(df.event_time.dt.date.unique())
#    plt.bar(df.event_time.dt.date.unique(),dfByDate)
#    plt.show()