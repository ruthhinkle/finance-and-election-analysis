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
voter_ID = []
county = []
candidate = []

#READ / INTERPRET
#open the CSV
with open(csvpath, mode= "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #define variable for header, 
    header = next(csvreader)
    csvdata = list(csvreader)

#define total votes, 
total_votes = 0
candidate_count = 0

#loop through rows
for row in csvdata:
        
    #count the total votes
    total_votes = [i,0]

    #count total votes per candidate w/ votes
    #identify election winner
    #month_count += 1
    
    #average changes
    #try:
        #sum_changes += int(csvdata[i+1][1]) - int(row[1])
    #except:
        #sum_changes += 0

    #append total votes
    total_votes.append(int(((row[0]))
    #dates.append(row[0])
    #define list

print(total_votes)
#DEFINE WHAT TO PRINT
#print # of months
# analysis_text = (
#     "Election Results \n"
#     "------------------------- \n"
#     f"Total Votes: {total_votes} \n"
#     "------------------------- \n"    
    
#     )
#     #list of candidates w/ vote total and percent of votes
    #winner
#print analysis text
print(analysis_text)

#PRINT EVERYTHING
#print to text file
with open("Analysis/analysis.txt", mode= "w") as txtfile:
    txtfile.write(analysis_text)