#imports
import os
import csv

csvpath = 'pybank/Resources/budget_data.csv'

dates = []
pnls = []

#reading files, appending to dates to find total number of months
with open(csvpath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader) #skipheader
    for row in csvreader:
        dates.append(row[0])
        pnls.append(int(row[1]))

print(f"The total number of months in the dataset is {len(dates)}")

#printing net profits/losses
if sum(pnls)>=0:
    print (f"The net total profits are ${sum(pnls)}")
else:
    print(f"The net total losses are {sum(pnls)}")

#%%
#changes in profits/losses

#loop through all profits and losses and find the difference
#append differences to list
#average the list
differences = []

for i in range(len(pnls)):
    difference = pnls[i] - pnls[i+1]
    differences.append(difference)
    if i == (len(pnls)-1):
        break
print(differences)
