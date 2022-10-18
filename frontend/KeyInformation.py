# Importing libraries
import pandas as pd
from collections import Counter
from collections import OrderedDict

# Reading local CSV file and assigning them to a list
df = pd.read_csv('/Users/calvinleow/Downloads/Oct19.csv')

brand_name = df[df.columns[3]].tolist()
price_list = df[df.columns[4]].tolist()

totalSales = len(price_list)
totalRevenue = int(sum(price_list))

# Putting Brand: Quantity into dictionary sorted from highest to lowest
brand_counter = dict(Counter(brand_name))
x = OrderedDict(sorted(brand_counter.items(), reverse = True, key=lambda t: t[1]))

# Retrieving top 5 brands with the highest quantities from the dictionary
n = 5
topNBrands = dict(list(x.items())[0: n])


print(f'Number of sales made in the month: {totalSales}')
print(f'Total amount of revenue made in the month: ${totalRevenue}')
print(f'Top 5 brands of the month by number of sales are: {topNBrands}')
