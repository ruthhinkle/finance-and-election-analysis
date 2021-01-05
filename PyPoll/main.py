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
#candidate = [2]


#READ / INTERPRET
#open the CSV
with open(csvpath, mode= "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #define variable for header, 
    header = next(csvreader)
    csvdata = list(csvreader)

#set voter count & candidate_count to zero
voter_count = 0
# candidate_count = 0

#loop through rows
for i,row in enumerate(csvdata):

    #count the total votes
    voter_count += 1
    
    #Add candidates names to dictionary and count their total votes each
    candidate_count = {}
    candidate = row [2]
    if candidate in candidate_count.keys():
        candidate_count[candidate] += 1
    else:
        candidate_count[candidate] = 1

    #Calculate percentage of the total vote for each candidate
    percentage = []
    for i in candidate_count:
        percentage = (float(candidate_count[i]) / voter_count) * 100
        results = (f"{i} {round(percentage,0)}%  ({candidate_count[i]})")


    
    #identify election winner

    #average changes
    #try:
        #sum_changes += int(csvdata[i+1][1]) - int(row[1])
    #except:
        #sum_changes += 0

    #append total votes
    #total_votes.append(int(((row[0]))
    #dates.append(row[0])
    #define list

    for key in candidate_count.keys():
        if candidate_count[key] == max(candidate_count.values()):
            winner = key


#DEFINE WHAT TO PRINT
analysis_text = (
    "Election Results \n"
    "------------------------- \n"
    f"Total Votes: {voter_count} \n"
    "------------------------- \n"
    f"{results} \n"
    "------------------------- \n"    
    f"Winner: {winner} \n"
)

# #PRINT EVERYTHING
#print to terminal
print(analysis_text)

#print to text file
with open("Analysis/analysis.txt", mode= "w") as txtfile:
    txtfile.write(analysis_text)