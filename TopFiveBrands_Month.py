# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from collections import OrderedDict

# Reading local CSV file and assigning them to a list
df = pd.read_csv('/Users/calvinleow/Downloads/Feb20.csv')
brand_name = df[df.columns[3]].tolist()
price_amount = df[df.columns[4]].tolist()

# Putting Brand: Quantity into dictionary sorted from highest to lowest
brand_counter = dict(Counter(brand_name))
x = OrderedDict(sorted(brand_counter.items(), reverse = True, key=lambda t: t[1]))

# Retrieving top 5 brands with highest quantities from the dictionary
n = 5
topNBrands = dict(list(x.items())[0: n])

# Data to plot
labels = []
sizes = []

for x, y in topNBrands.items():
    labels.append(x)
    sizes.append(y)

# Plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

plt.axis('equal')
plt.show()


