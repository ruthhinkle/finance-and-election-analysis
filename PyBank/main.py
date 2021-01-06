#PYBANK CHALLENGE

#Import os & CSV
import os
import csv

#Set file path
csvpath = os.path.join("Resources", "budget_data.csv")

#Create list for dates & profits/losses
dates = []
profit_losses = []

#READ & INTERPRET THE DATA
#Open the CSV
with open(csvpath, mode= "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #define variable for header & Csv data
    header = next(csvreader)
    csvdata = list(csvreader)

#efine month count and sum changes
sum_changes = 0
month_count = 0

#Loop through rows, SOURCE: enumerate function suggested by tutor
for i,row in enumerate(csvdata):
        
    #sum count of months
    month_count += 1
    
    #sum total profit/losses
    total_change = sum(profit_losses)

    #average changes
    try:
        sum_changes += int(csvdata[i+1][1]) - int(row[1])
    except:
        sum_changes += 0

    #append total profit/loss
    profit_losses.append(int(row[1]))
    dates.append(row[0])

#DEFINE WHAT TO PRINT
analysis_text = (
    "Financial Analysis \n"
    "------------------------------ \n"
    f"Total Months: {month_count} \n"
    f"Total: ${total_change} \n"
    f"Average Change: ${round(sum_changes/month_count, 2)} \n"
    f"Greatest Increase in Profits: {dates[profit_losses.index(max(profit_losses))]} ${max(profit_losses)} \n"
    f"Greatest Decrease in Losses: {dates[profit_losses.index(min(profit_losses))]} ${min(profit_losses)} \n"

    )

#PRINT EVERYTHING
#Print analysis text
print(analysis_text)

#Print to text file
with open("Analysis/analysis.txt", mode= "w") as txtfile:
    txtfile.write(analysis_text)