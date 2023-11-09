#imports
import os 
import csv
import numpy as np

filepath = 'pypoll/Resources/election_data.csv'

ballot_id = []
county = []
candidates = []

#determine the total number of votes by the length of the columns
#find candidates by looking at unique entries of the list
with open(filepath, encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    for row in csvreader:
        ballot_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])
print("\n Election Results \n ----------------- \n")
print(f"Total votes: {len(ballot_id)} \n ----------------- \n")

uniq_candidates = np.unique(candidates)
candidate_votes = np.zeros(len(uniq_candidates))

for cand_i in range(len(uniq_candidates)):
    for name in candidates:
        if name == uniq_candidates[cand_i]:
            candidate_votes[cand_i] += 1
    print(f"{uniq_candidates[cand_i]}: {candidate_votes[cand_i]/len(ballot_id)*100}% {candidate_votes[cand_i]} \n")

print("---------------------")
print(f"Winner: {uniq_candidates[candidate_votes.argmax()]}")

