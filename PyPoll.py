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
candidates_options =[]
candidate_votes ={}

winning_count =0
winning_candidate=""
winning_percentage = 0
file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)

    for row in file_reader:
        total_Votes = total_Votes+1
        candidates_name = row[2]
        if candidates_name not in candidates_options:
            candidates_options.append(row[2]) #add unique candidates
            candidate_votes[candidates_name] =0  #add candidate name as dictionary key
        candidate_votes[candidates_name] +=1  # add votes for each candidate as a value in the dictionary 

    with open(file_to_save, 'w') as election_analysis:
        election_results = (
            f"\nElection Results\n"
            f"---------------------\n"
            f"Total Votes {total_Votes:,}\n"
            f"......................\n")
        election_analysis.write(election_results)
        
    
        # % of votes for each candidate 
        for candidate_name in candidate_votes:
            votes = candidate_votes[candidate_name]  #get value from dictionary 
            votes_percentage = float(votes)/float(total_Votes) *100 #calculate percentage of votes for each candidate 
            #print(f"{candidate_name:} {votes_percentage} % ({votes:,})\n" )
            candidate_results = (f"{candidate_name}: {votes_percentage:.1f}% ({votes:,})\n")
            election_analysis.write(candidate_results)


            #find out the winning candidate and winning vote %
            if (votes > winning_count) and (votes_percentage>winning_percentage):
                winning_count = votes
                winning_percentage = votes_percentage
                winning_candidate = candidate_name

    #print(f"Winning candidate is {winning_candidate} with winning count {winning_count:,} and winning percentage {winning_percentage:.2f} ")

election_analysis.close

