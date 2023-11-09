#%%
#imports
import os
import csv
import numpy as np

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

##%

#changes in profits/losses

#loop through all profits and losses and find the difference
#append differences to list
#average the list

differences = []
max = 0
min = 0

for i in range(len(pnls)):
    difference = pnls[i+1] - pnls[i]
    differences.append(difference)
    if difference > max:
        max = difference
        max_i = i+1
    if difference < min:
        min = difference
        min_i = i+1
    if i == (len(pnls)-2):
        break
print(f'The average of all these differences is {np.mean(differences)} \n')

print(f"The greatest increase occurred at {max_i} when the value increased from {pnls[max_i-1]} to {pnls[max_i]} \n where the difference was {max}")
print(f"This is an increase of {(max/pnls[max_i+1])*100}%!")
print(f"This occurred during the month {dates[max_i]} \n")

print(f"The greatest decrease occurred at {min_i} when the value decreased from {pnls[min_i-1]} to {pnls[min_i]} \n where the difference was {min}")
print(f"This is an decrease of {(min/pnls[min_i+1])*100}%!")
print (f"This occurred during the month {dates[min_i]}")


# %%
