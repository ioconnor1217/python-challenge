# Import modules
import csv
import os

# Declare files to load and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "Analysis.txt")

# Initialize variables
total_votes = 0
winning_candidate = ""
winning_count = 0

# Define lists and dictionaries
candidate_votes = {}
candidates = []

# Open and read the csv
with open(file_to_load) as data:
    reader = csv.reader(data)

    # Skip the header row
    header = next(reader)

    # Loop through each row
    for row in reader:

        # Increment total votes
        total_votes += 1

        # Get candidate's name
        candidate_name = row[2]

        # If not already in the list, add candidate 
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Write the results to the txt file
with open(file_to_output, "w") as txt:

    # Print the total vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")

    # Write the total vote count to txt file
    txt.write(election_results)

    # Loop to determine the winner
    for candidate in candidate_votes:

        # Get vote count and calculate percentage
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt.write(candidate_results)

    # Display the winning candidate
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )

    # Print the winning candidate
    print(winning_candidate_summary)

    # Save the winning candidate to txt file
    txt.write(winning_candidate_summary)
    