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

#open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #loop through rows
    for row in csvreader:

        #define variables
        months = int(csvfile[0])
        
        #count months
        print(months)