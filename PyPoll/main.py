# PyPoll: Module 3 challenge - Election Results

# Calculate: total votes, list of candidates with votes, % of votes each candidate received, total number of votes for each candidate, winner of the election

# Import csv file.  Comma delimited with Ballot ID, County, Candidate
import os
import csv

csvpath = os.path.join(".", "Resources", "election_data.csv")

# Set file to write output
file = "./analysis/election_results.txt"

# Set variables for calculations
total_votes = 0
candidates = []
votes = []
percent_votes = []

# Use csv file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csvheader = next(csvreader)

    for row in csvreader:

        # Select total votes
        total_votes += 1

        #Select all candidates receiving votes and initialize their vote counts
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)
            percent_votes.append(0)

        #Add votes for each candidate
        candidate_index = candidates.index(row[2])
        votes[candidate_index] += 1

csvfile.close()

# Calculate % of votes for each candidate
for candidate in candidates:
    percent_votes[candidates.index(candidate)] = round(votes[candidates.index(candidate)] / total_votes *100, 3)

# Determine Winner
max_votes = max(votes)
winner_index = votes.index(max_votes)
winner = candidates[winner_index]

# Write and Print Results
header1 = "Election Results"
header2 = "------------------------------"

results = [f'{header1}\n',
           f'{header2}\n',
           f'Total Votes: {total_votes}\n',
           f'{header2}\n',
           ]

with open(file, "w") as text:
    text.writelines(results)
    for x in range(0, len(candidates)):
        text.write(f'{candidates[x]}: {percent_votes[x]}% ({votes[x]})\n')
    text.write(f'{header2}\n')
    text.write(f'Winner: {winner}\n')
    text.write(f'{header2}')
text.close()


print(f'{header1}\n')
print(f'{header2}\n')
print(f'Total Votes: {total_votes}\n')
print(f'{header2}\n')

for x in range(0, len(candidates)):
    print(f'{candidates[x]}: {percent_votes[x]}% ({votes[x]})\n')

print(f'{header2}\n')
print(f'Winner: {winner}\n')
print(f'{header2}')
