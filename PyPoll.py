#Get data of total number of votes cast
#Get list of all the candidates
#Get the votes for each candidated
#Get the total numnber of votes
#Get the percentage of votes recieved by each candidate(eachCandidateVote/totalNumberOfVotes)

import csv
import os
#import sys 

#open the election data file
#file_to_load = 'c:\Users\shail\Election_Analysis\Resources\election_results.csv'
#file_to_save = r'c:\Users\shail\Election_Analysis\analysis\election_analysis.txt'

file_to_load = os.path.join("Resources", "election_results.csv")  #OS specific utilities
total_Votes = 0
file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        total_Votes = total_Votes+1
    print(total_Votes)
   
    
   
with open(file_to_save, 'w') as election_analysis:
    election_analysis.write("Counties in the Election")
    election_analysis.write("\n------------------------")
    election_analysis.write("\nArapahoe\nDenver\nJefferson")
    
    

election_analysis.close

