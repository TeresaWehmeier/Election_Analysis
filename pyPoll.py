# the data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates wo received votes
#3. The pcercentage of votes each candidate won
#4. Tht total number of votes each candidate won.
#5. GThe winner of the election based on popular vote.

# Import the datetime class from the datetime module
#import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()

# Print the present time
#print("The time right now is ", now)

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

#1. Intialize the total vote counter
total_votes = 0

candidate_options = []

candidate_votes = {}

# winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.

with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Print the header rowl
    headers = next(file_reader)
    #print(headers)

    # print each row in the CSV file
    for row in file_reader:
        total_votes += 1

    #print(total_votes)

    # Print the candidate name from each row
        candidate_name = row[2]
    #candidate_options.append(candidate_name)

    # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
            # add a vote to theat cadidates count
        candidate_votes[candidate_name] += 1
for candidate_name in candidate_votes:
    # 2 Retrieve vote count of candidate
    votes = candidate_votes[candidate_name]
    # 3 calculate the precentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. print the candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent = vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # set the winning candidate equal to the candidates name
        winning_candidate = candidate_name
# print out the winning candidate, vote count and percentage to the terminal
#print(f"{winning_candidate} is the winner with {winning_count} votes, or {winning_percentage:.1f}% of the vote.")
winning_candidate_summary = (
    f"------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------------------\n")
print(winning_candidate_summary)


    