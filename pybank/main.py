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

#printing total number of months
print(f"The total number of months in the dataset is {len(dates)}")

#printing net profits/losses
if sum(pnls)>=0: #for profits
    print (f"The net total profits are ${sum(pnls)}")
else: #prints losses if neg value
    print(f"The net total losses are {sum(pnls)}")

#Calculating changes in profits/losses:


differences = []
max = 0
min = 0

#loop through all profits and losses and find the difference
for i in range(len(pnls)):
    difference = pnls[i+1] - pnls[i]

    #append differences to list
    differences.append(difference)

    #finding max and min differences
    if difference > max:
        max = difference
        max_i = i+1
    if difference < min:
        min = difference
        min_i = i+1
    if i == (len(pnls)-2):
        break

#printing the average, max, min and the month during when it occurred
print(f'The average of all these differences is {np.mean(differences)} \n')

print(f"The greatest increase occurred at {max_i} when the value increased from {pnls[max_i-1]} to {pnls[max_i]} \n where the difference was {max}")
print(f"This is an increase of {(max/pnls[max_i+1])*100}%!")
print(f"This occurred during the month {dates[max_i]} \n")

print(f"The greatest decrease occurred at {min_i} when the value decreased from {pnls[min_i-1]} to {pnls[min_i]} \n where the difference was {min}")
print(f"This is an decrease of {(min/pnls[min_i+1])*100}%!")
print(f"This occurred during the month {dates[min_i]}")

#Taking all outputs and creating a text file within pybank folder
with open('pybank/analysis.txt', 'w') as file:
    file.write(f"Total months: {len(dates)}\n")

    if sum(pnls)>=0:
        file.write (f"Net profits: ${sum(pnls)}\n")
    else:
        file.write (f"Net losses: ${sum(pnls)}\n")

    
    file.write(f'Average Change: {np.mean(differences)} \n \n')
    file.write(f"The greatest increase occurred at {max_i} when the value increased from {pnls[max_i-1]} to {pnls[max_i]} \n where the difference was ${max}\n")
    file.write(f"This is an increase of {int((max/pnls[max_i+1])*100)}%! \n")
    file.write(f"This occurred during the month {dates[max_i]} \n \n")

    file.write(f"The greatest decrease occurred at {min_i} when the value decreased from {pnls[min_i-1]} to {pnls[min_i]} \n where the difference was ${min}\n")
    file.write(f"This is an decrease of {int((min/pnls[min_i+1])*100)}%! \n")
    file.write(f"This occurred during the month {dates[min_i]} \n")
# %%
