# Modules
import os
import csv

# Path to collect data from the Resources folder
dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, 'Resources/budget_data.csv')


# Variables
total_months = 0
total_volume = 0
current_month = 0
previous_month = 0

# Lists to store data
changeList = []
monthList = []

# Open the CSV
with open(filepath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Loop through the rows
    for row in csvreader:  
        total_months += 1
        total_volume += int(row[1])    
        #average changes = average of the current row's volume - the previous row's volume (that needs to be stored in a variable) divided by month
        current_month = int(row[1])
        monthly_change = (current_month - previous_month)
        changeList.append(monthly_change)
        #len(changeList)
        previous_month = int(row[1])
        #print(changeList)
        monthList.append(row[0])
        
changeList.pop(0)
maxindex = changeList.index(max(changeList))
#print(monthList[maxindex +1])
minindex = changeList.index(min(changeList))
#print(monthList[minindex +1])

#Print to the screen 
print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_volume}")
print(f"Average Change: ${round(sum(changeList)/len(changeList))}")
print(f"Greatest Increase in Profits: {monthList[maxindex +1]} $({(max(changeList))})")
print(f"Greatest Decrease in Profits: {monthList[minindex +1]} $({(min(changeList))})")

# Specify the file to write to
output_path = os.path.join(dirname, "Output", "PyBank.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as PyBank:

    # Initialize csv.writer
    csvwriter = csv.writer(PyBank, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-----------------------'])
    csvwriter.writerow([f'Total Months: {total_months}'])
    csvwriter.writerow([f'Total: ${total_volume}'])
    csvwriter.writerow([f'Average Change: ${round(sum(changeList)/len(changeList))}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {monthList[maxindex +1]} $({(max(changeList))})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {monthList[minindex +1]} $({(min(changeList))})'])

