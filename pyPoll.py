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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

# Print the header rowl
    headers = next(file_reader)
    print(headers)

    # print each row in the CSV file
    #for row in file_reader:
        #print(row)
    