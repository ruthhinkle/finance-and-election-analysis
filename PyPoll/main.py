# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
    # Election Results
    # -------------------------
    # Total Votes: 3521001
    # -------------------------
    # Khan: 63.000% (2218231)
    # Correy: 20.000% (704200)
    # Li: 14.000% (492940)
    # O'Tooley: 3.000% (105630)
    # -------------------------
    # Winner: Khan
    # -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#import os & CSV
import os
import csv

#set file path
csvpath = os.path.join("Resources", "election_data.csv")
dates = []
profit_losses = []

#READ / INTERPRET
#open the CSV
with open(csvpath, mode= "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #define variable for header, 
    # header = next(csvreader)
    # csvdata = list(csvreader)

#define month count and sum changes
sum_changes = 0
month_count = 0

#loop through rows
for i,row in enumerate(csvdata):
        
    #sum count of months
    month_count += 1
    
    #average changes
    try:
        sum_changes += int(csvdata[i+1][1]) - int(row[1])
    except:
        sum_changes += 0

    #append total profit/loss
    profit_losses.append(int(row[1]))
    dates.append(row[0])
    #define list



#DEFINE WHAT TO PRINT
#print # of months
analysis_text = (
    "Financial Analysis \n"
    f"Total Months: {month_count} \n"
    f"Total: {month_count} \n"
    f"Average Change: ${round(sum_changes/month_count, 2)} \n"
    f"Greatest Increase in Profits: {dates[profit_losses.index(max(profit_losses))]} {max(profit_losses)} \n"

    )
#print analysis text
print(analysis_text)

#PRINT EVERYTHING
#print to text file
with open("Analysis/analysis.txt", mode= "w") as txtfile:
    txtfile.write(analysis_text)