import os
import csv

# Set path for file
election_results = os.path.join("..", "python-challenge0", "Resources_CSV", "election_data.csv")

# Declare Variables
total_votes = 0
Stockham_votes = 0
DeGette_votes = 0
Doane_votes = 0

# open csv
with open (election_results, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter =",")

    # Read the header row first
    header = next(reader)

    # Loop through each row
    for row in reader:
        
        # Count voter IDs and store total votes
        total_votes +=1

        # Count amount of times candidate name appears in list
        if row[2] == "Charles Casper Stockham":
            Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            Doane_votes +=1

    # Find percentages for each candidate
    Stockham_percent = (Stockham_votes/total_votes) *100
    DeGette_percent = (DeGette_votes/total_votes) *100
    Doane_percent = (Doane_votes/total_votes) *100

    # Find winner of election

    # Print summary
    print(f"Election Results")
    print(f"---------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"---------------------------")
    print(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham_votes})")
    print(f"Diana DeGette: {DeGette_percent}% ({DeGette_votes})")
    print(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_votes})")
    print(f"---------------------------")
    print(f"Winner:")
    print(f"---------------------------")

    # Export text file 
    output_pypollfile = os.path.join("..", "python-challenge0", "Resources_CSV", "PyPoll_Mod3.txt")
    with open(output_pypollfile, "w") as file:
        file.write(f"Election Results")
        file.write(f"---------------------------")
        file.write(f"Total Votes: {total_votes}")
        file.write(f"---------------------------")
        file.write(f"Charles Casper Stockham: {Stockham_percent}% ({Stockham_votes})")
        file.write(f"Diana DeGette: {DeGette_percent}% ({DeGette_votes})")
        file.write(f"Raymon Anthony Doane: {Doane_percent}% ({Doane_votes})")
        file.write(f"---------------------------")
        file.write(f"Winner:")
        file.write(f"---------------------------")



    





