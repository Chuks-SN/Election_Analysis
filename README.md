# Election_Analysis
### Overview of Election Audit 
The purpose of the election audit is to provide the following information to the Colorado Board of Elections:
The total number of votes cast
A complete list of candidates who received votes
The total number of votes each candidates received
The percentage of votes each candidate won
The winner of the election based on popular vote

### Election Audit Results 
#### Number of votes cast in the congressional election
From the results of the election, the total number of votes count was 369,711. 
In the code, the total vote count was first initialized to zero, and the command 'total_votes = total_votes + 1' was used to get the total number of votes in the election. 

#### Breakdown of number of votes and percentage of votes for each county
###### Jefferson
Number of votes: 38,855
Percentage of votes: 10.5%
###### Denver 
Number of votes: 306,055
Percentage of votes: 82.8%
###### Arapahoe
Number of votes: 24,801
Percentage of votes: 6.7%

##### County with the largest number of votes
Denver 

#### Breakdown of number and percentage of votes for each candidate
###### Charles Casper 
Number of votes: 85,213
Percentge of votes: 23.0%
###### Diana DeGette
Number of votes: 272,892
Percentage of votes: 73.8%
###### Raymon Anthony Doane
Number of votes: 11,606
Percentage of votes: 3.1%

##### Winner of the election
This winner of the election was Diana DeGette with 272,892 votes which translated to 73.8% of the total votes.

### Election-Audit Summary
The most critical part of an election is result collation. With little modifications and refactoring, this code can be employed in elections with larger vote counts i:e state or national elections. 
One of the ways the code can be modified for this purpose is to replace the "county" varibales (county_list, county_dict, e.t.c) with a state_list and state_dictionay e.t.c, so that the code pulls that information from a corresponding CVS file. 

The code can also be used for elections in other counties asides Jefferson, Denver and Arapahoe. This can be done by replacing the "election_result_cvs" in command line 9 with the name of a conrresponding cvs file. 




