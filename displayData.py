# Python program to convert
# CSV to HTML Table


import pandas as pd
import pandas as pandasForSortingCSV

# assign dataset
csvData = pandasForSortingCSV.read_csv("mergedData.csv")
										

# sort data frame
csvData.sort_values(["brand", "price"],
					axis=0,
					ascending=[True, True],
					inplace=True)

to_drop = ['event_time', 'product_id', 'user_id', 'user_session']
csvData.drop(to_drop, inplace=True, axis=1)


# to save as html file
# named as "Table"
csvData.to_html("TableSorted.html")

# assign it to a
# variable (string)
html_file = csvData.to_html()
