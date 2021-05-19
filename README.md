# Election_Analysis

## Overview of Project

### Purpose
The purpose of this election audit analysis is :
1. To find out how each county performed based on the percentage of voter turnout
2. To find the performance of each candidate based on the number of votes they reieved. 

## Results

### Election Audit Results
- How many votes were cast in this congressional election?
  369,711 were casted in the congressional election.
  
- Provide a breakdown of the number of votes and the percentage of total votes 
  for each county in the precinct.
  1. More than 80% of the votes were casted for Denver county followed by Jefferson and Arapahoe.
     
	 - Denver : 82.8% : 306,055
	 - Jefferson : 10.5% : 38,855
	 - Arapahoe : 6.7% : 24,801
	 
- Which county had the largest number of votes?
  Denver has the largest number of votes(306,055)
  
- Provide a breakdown of the number of votes and the percentage of the
  total votes each candidate received.
  1. Diana DeGette recieved almost 70% of the total votes followed by Charles and Raymon
  
     - Charles Casper Stockham: 23.0% (85,213)
     - Diana DeGette: 73.8% (272,892)
	 - Raymon Anthony Doane: 3.1% (11,606)
  
- Which candidate won the election, what was their vote count, and what was 
  their percentage of the total votes?
  Diana DeGette won the election with 272,892 vote count which is 73.8% if the total votes 
  
![](./Resources/ElectionResults.PNG)
  

## Summary

1. Business Proposal :
   - Currently we are appending values inside 2 dictionaries, *candidate_votes* and *county_votes and we have written
     2 if loops. As the number of rows are same for all the 3 columns in the data, we can only write 1 if condition 
	 to check both county_name and candidate_name. This way if more columns are added in our data, we can iterate through 
	 all the data and populate dictionaries at once. 
   - Currently we only have 3 counties and 3 candidates so it is easy to view the results in text file without formatting.
     We can edit the script in such a way that it creates a table inside the text file to show votes for all the county and
	 candidates in tabular form.
	 
  
	 
