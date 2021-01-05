#Calculate each of the following:
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
    #As an example, your analysis should look similar to the one below:
        #Financial Analysis
        #----------------------------
        #Total Months: 86
        #Total: $38382578
        #Average  Change: $-2315.12
        #Greatest Increase in Profits: Feb-2012 ($1926159)
        #Greatest Decrease in Profits: Sep-2013 ($-2196167)
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#import os & CSV
import os
import csv

#set file path
csvpath = os.path.join("Resources", "budget_data.csv")
dates = []
profit_losses = []

#READ & INTERPRET THE DATA
#open the CSV
with open(csvpath, mode= "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #define variable for header & Csv data
    header = next(csvreader)
    csvdata = list(csvreader)

#efine month count and sum changes
sum_changes = 0
month_count = 0

#Loop through rows
#Source: Enumerate function suggested by tutor
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
#print # of months
analysis_text = (
    "Financial Analysis \n"
    "------------------------------ \n"
    f"Total Months: {month_count} \n"
    f"Total: ${total_change} \n"
    f"Average Change: ${round(sum_changes/month_count, 2)} \n"
    f"Greatest Increase in Profits: {dates[profit_losses.index(max(profit_losses))]} ${max(profit_losses)} \n"
    f"Greatest Decrease in Losses: {dates[profit_losses.index(min(profit_losses))]} ${min(profit_losses)} \n"

    )
#print analysis text
print(analysis_text)

#PRINT EVERYTHING
#print to text file
with open("Analysis/analysis.txt", mode= "w") as txtfile:
    txtfile.write(analysis_text)