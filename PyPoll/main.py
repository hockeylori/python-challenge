# Modules
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv.csv")
path = "/Users/lorishannon/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

# Variables
total_votes = 0
votes = 0

# Dictionaries to store key value pairs 
candidates = {}

# Open the CSV
with open(path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Loop through the rows
    for row in csvreader:  
        total_votes += 1
        candidates_name = row[2]
        candidate_votes = candidates.get(candidates_name, 0)
        candidates[candidates_name] = candidate_votes + 1

# Print to screen       
# printvotes = "{:.3f}".format( value/total_votes * 100 )      
print("Election Results")
print("-----------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------")

for key, value in candidates.items():
    percent_won = value/total_votes
    print(f"{key}: {percent_won * 100}% ({value})")
    if value > votes: 
        votes = value
        winner = key

print("-----------------------")
print(f"Winner: {winner}")
print("-----------------------")


#Specify the file to write to
output_path = os.path.join("/Users/lorishannon/Desktop/python-challenge/PyPoll/Output", "PyPoll.csv")

#Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as PyPoll:

    #Initialize csv.writer
    #csvwriter = csv.writer(PyPoll, delimiter=',')
    csvwriter = csv.writer(PyPoll, delimiter=',')

    #Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow(['Total Votes:'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow([('total_votes')])
    csvwriter.writerow(['-----------------------'])
    #csvwriter.writerow([('key'): ('(percent_won * 100)')% ({value})'])
    csvwriter.writerow(['-----------------------'])
    #csvwriter.writerow(['Winner: ('winner')])
    csvwriter.writerow(['-----------------------'])

