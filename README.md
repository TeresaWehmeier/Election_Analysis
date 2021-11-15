# Election Audit Analysis

## Project Overview
A Colorado election commission requests an election audit and analysis of a local congressional election. The expected results should include:
- Total votes
- Total votes and percentage by county
- County with the highest voter turnout
- Candidate votes and perentage of total votes
- Winner of the election with total and percentage of votes

## Resources
- Data source: election_results.csv
- Software: Python 3.9.7; Visual Studio Code 1.6.22

## Election-Audit Results:
The project requirements utilize a Python script that reads the election data set, compiles the requested information, and prints the results to a text file and a terminal screen.  
1. Total votes cast in the congressional election
  - Total votes cast was 369,711. the Python script used to obtain these results is shown in this image; the results are presented in the text file and on the terminal:
     <img src = "Images/python_total_votes_for_statement.png" width = "30%" height = "10%">
2. Breakdown of the number of votes and percentage of total votes for each county in the county.
  - Three counties had voter returns in the data file provided; they were Jefferson, Denver and Arapahoe. Of the 369,711 votes cast, 10.5% (38,855) were from Jefferson, 82.8% (306,055) were from Denver and 6.7% (24,801) were from Arapahoe. The Python code used to derive these results is provided in the image below.
3. Which county had the largest number of votes?
  - The county with the largest voter turnout was in Denver County with a turnout rate of 82.8%. The image provided is from the text file, but is also presented on the terminal.
  <img src = "https://github.com/TeresaWehmeier/Election_Analysis/blob/main/Images/text_file_results_county_with_high_turnout.png" width = "30%" height = "10%">
7. The total number of votes and percentage each candidate received.
8. Identify the winner of the election, their vote count and percentage of total votes.

## Election-Audit Summary
The analysis of the election shows:
1. There were 369,711 votes cast
2. The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Done
3. The candidate results were:
  - Charles Casper Stockham received 23.0%, or 85,213 votes
  - Diana DeGette received 73.8%, or 272,892 votes
  - Raymon Anthony Doane received 3.1%, or 11,606 votes
4. The winner of the election was:
  - Diana Degette who received 73.8% of the vote and 272,892 votes.

