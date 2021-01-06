#PYPOLL CHALLENGE

#import os & CSV
import os
import csv

#set file path
csvpath = os.path.join("Resources", "election_data.csv")

#READ / INTERPRET

#Create Dictionary for Candidates
candidate_count = {}

#Open the CSV
with open(csvpath, mode= "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #define variable for header, 
    header = next(csvreader)
    csvdata = list(csvreader)

#Initialize count of total votes to zero
voter_count = 0

#Loop through the rows, SOURCE: enumerate function suggested by tutor
for i,row in enumerate(csvdata):

    #Count the total number of votes
    voter_count += 1
    
    #Add candidates to candidate_count dictionary and count the votes they received
    candidate = row [2]
    if candidate in list(candidate_count.keys()):
        candidate_count[candidate] += 1
    else:
        candidate_count[candidate] = 1

    #Calculate percentage of votes per candidate and write results list to print
    results = ""
    for candidate in list(candidate_count.keys()):
        c_percentage = (float(candidate_count[candidate]) / voter_count) * 100
        c_results = str(f"{candidate} {round(c_percentage,0)}%  ({candidate_count[candidate]}) \n")
        results += c_results 

    #Determine the winner of the popular vote
    for key in candidate_count.keys():
        if candidate_count[key] == max(candidate_count.values()):
            winner = key

#DEFINE WHAT TO PRINT
analysis_text = (
    "Election Results \n"
    "------------------------- \n"
    f"Total Votes: {voter_count} \n"
    "------------------------- \n"
    f"{results}"
    "------------------------- \n"    
    f"Winner: {winner} \n"
)

#PRINT EVERYTHING
#Print to terminal
print(analysis_text)

#Print to text file
with open("Analysis/analysis.txt", mode= "w") as txtfile:
    txtfile.write(analysis_text)