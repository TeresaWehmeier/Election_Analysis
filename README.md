# Election Audit Analysis

## Project Overview
A Colorado election commission requests an election audit and analysis of a local congressional election. The expected results should include:
- Total votes
- Total votes and percentage by county
- County with the highest voter turnout
- Candidate votes and percentage of total votes
- Winner of the election with total and percentage of votes

### Resources
- Data source: election_results.csv
- Software: Python 3.9.7; Visual Studio Code 1.6.22

### Election-Audit Results:
The project requirements utilize a Python script that reads the election data set, compiles the requested information, and prints the results to a text file and a terminal screen.  
1. Total votes cast in the congressional election
  - Total votes cast was 369,711. the Python script used to obtain these results is shown in this image; the results are presented in the text file and on the terminal:
  
     <img src = "Images/python_total_votes_for_statement.png" width = "30%" height = "10%">
     
2. Breakdown of the number of votes and percentage of total votes for each county in the precint.
  - Three counties had voter returns in the data file provided; they were Jefferson, Denver and Arapahoe. Of the 369,711 votes cast, 10.5% (38,855) were from Jefferson; 82.8% (306,055) were from Denver; and 6.7% (24,801) were from Arapahoe. The portion of Python code used to derive these results is provided below.

      for county_name in county_votes:
        **6b: Retrieve the county vote count.**
        votes_turnout = county_votes.get(county_name)
        turnout_percent = float(votes_turnout / total_votes) * 100
        county_results = (
            f"{county_name}: {turnout_percent:.1f}% and {votes_turnout:,} votes.\n")
        print(county_results)
        txt_file.write(county_results)
  
3. Which county had the largest number of votes?
  - The county with the largest voter turnout was in Denver County with a turnout rate of 82.8%. The image provided is from the text file, but is also presented on the terminal when running the Python script.

  <img src = "Images/text_file_results_county_with_high_turnout.png" width = "30%" height = "10%">

4. The total number of votes and percentage each candidate received.
  - There were three candidates in the election audit. The results by candidate are provided as they appear in the text file and on the terminal screen.
    - Charles Casper Stockham received 23.0%, or 85,213 votes
    - Diana DeGette received 73.8%, or 272,892 votes
    - Raymon Anthony Doane received 3.1%, or 11,606 votes

5. Identify the winner of the election, their vote count and percentage of total votes.
  - The winner of the election audit wsa Diana DeGette, with 73.8% (272,892) of the vote. In the image below, the Python code is provided to describe how the results were derived:

  <img src = "Images/python_winning_candidate.png" width = "30%" height = "10%">

### Text File Results
 
  <img src = "Images/summary_election_audit_text_file.png" width = "30%" height = "10%">
 
### Election-Audit Summary
The provided Python code is robust and can be used on a much wider scale. The data provided for this audit included only three counties in the state, but the audit program can accomodate much larger data sets, and should be expanded to all counties in the state.

The election commission may wish to consider some additional functionality to the Python script used to develop this audit. For example, it might be interesting to discover the winning candidate by county. By simply adding an additional "if" statement to the current code, the number of candidates per county could be tallied, providing deeper insight into the voting patterns within a given county. It would also be interesting to find voter turnout by polling location. A polling location column would need to be added to the election_results_csv file, but the ability to drill deeply into polling locations would provide information on voter volume, and may assist in planning future voting locations based on the analysis. For example, the analysis may reveal that some polling locations are under utilized, while others have more voter participation than staff can manage.



