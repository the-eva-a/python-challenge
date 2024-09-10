import csv 

candidates = {}
# Open the election_data file
with open('PyPoll/Resources/election_data.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    next(reader) # Skip header row
    
    #  Calculate the number of votes for each candidate 
    for row in reader:
        candidate = row[2]
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1
    
total_votes = sum(candidates.values())

results = (f"Election Results\n"
           "--------------------------\n"
           f"Total Votes: {total_votes}\n"
           "--------------------------\n")
# Add each candidates voting results to the output string
for key, value in candidates.items():
    results += (f"{key}: {round(value / total_votes * 100, 2)}% ({value})\n")

# Find the candidate with the maximum votes
winner = max(candidates, key=candidates.get)

results += (f"--------------------------\n"
            f"Winner: {winner}\n"
            "--------------------------")

print(results) # Show the results in the terminal

with open("PyPoll/analysis/PyPoll Analysis.txt", "w") as f:
    f.write(results) # Write the results in the analysis folder
