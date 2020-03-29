# Modules
import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("..", "Resources", "budget_data.csv")
path = "/Users/lorishannon/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

# Variables
total_months = 0
total_volume = 0
current_month = 0
previous_month = 0

# Lists to store data
changeList = []

# Open the CSV
with open(path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Loop through the rows
    for row in csvreader:  
        total_months += 1
        total_volume += int(row[1])    
        #average changes = average of the current row's volume - the previous row's volume (that needs to be stored in a variable) divided by month
        current_month += int(row[1])
        previous_month = int(row[1])
        monthly_change = (current_month - previous_month)
        changeList = monthly_change
        #changeList.append(total_volume)
        #len(changeList)
        print(changeList)

# save the output file path
output_file = os.path.join("output.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Financial Analysis"])


#Print to the screen 
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_volume}")
print(f"Average Change: ({changeList} / {total_volume}))")
print(f"Greatest Increase in Profits: (max( {changeList} )")
print(f"Greatest Decrease in Profits: (min( {changeList} )")