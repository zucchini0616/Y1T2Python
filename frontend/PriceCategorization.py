# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd


# Reading local CSV file and assigning them to a list
df = pd.read_csv('/Users/calvinleow/Downloads/Feb20.csv')
price_amount = df[df.columns[4]].tolist()

# Assigning all counters to 0
purchasesBelow50 = 0
purchasesBelow100 = 0
purchasesBelow250 = 0
purchasesBelow500 = 0
purchasesBelow1000 = 0
purchasesEqualBelow2000 = 0
purchasesAbove2000 = 0


# Counting through the list
for i in price_amount:
    if i < 50:
        purchasesBelow50 += 1
    elif i < 100:
        purchasesBelow100 += 1
    elif i < 250:
        purchasesBelow250 += 1
    elif i < 500:
        purchasesBelow500 += 1
    elif i < 1000:
        purchasesBelow1000 += 1
    elif i <= 2000:
        purchasesEqualBelow2000 += 1
    elif i > 2000:
        purchasesAbove2000 +=1

print(f'The number of purchases below $50 are: {purchasesBelow50}')
print(f'The number of purchases below $100 are: {purchasesBelow100}')
print(f'The number of purchases below $250 are: {purchasesBelow250}')
print(f'The number of purchases below $500 are: {purchasesBelow500}')
print(f'The number of purchases below $1000 are: {purchasesBelow1000}')
print(f'The number of purchases below or equal to $2000 are: {purchasesEqualBelow2000}')
print(f'The number of purchases more than $2000 are: {purchasesAbove2000}')

# function to add value labels
def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i] // 2, y[i], ha='center')


if __name__ == '__main__':
    # creating data on which bar chart will be plot
    x = ["< $50", "< $100", "< $250",
         "< $500", "< $1000", "<= $2000", "> $2000"]

    y = [purchasesBelow50, purchasesBelow100, purchasesBelow250, purchasesBelow500,
         purchasesBelow1000, purchasesEqualBelow2000, purchasesAbove2000]

    # setting figure size by using figure() function
    plt.figure(figsize=(10, 5))

    # making the bar chart on the data
    plt.bar(x, y)

    # calling the function to add value labels
    addlabels(x, y)

    # giving title to the plot
    plt.title("Price Categorization")

    # giving X and Y labels
    plt.xlabel("Price")
    plt.ylabel("Number of Purchases")

    # visualizing the plot
    plt.show()