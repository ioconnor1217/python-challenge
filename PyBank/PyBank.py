# Dependencies
import csv
import os

# Declare files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("Analysis", "Analysis.txt")

# Init variables
total_months = 0
total_net = 0
prev_net = 0
net_change_list = []
change_date = []
increase = ["", 0]
decrease = ["", 9999999999999999999]

# Open and read the csv
with open(file_to_load) as data:
    reader = csv.reader(data)

    # Skip the header row
    header = next(reader)

    # Extract first row
    first_row = next(reader)
    total_months += 1

    # Track the total and net change
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Update the total net amount by adding the current row's profit/loss value
        total_net += int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list.append(net_change)
        change_date.append(row[0])

        # Calculate the greatest increase
        if net_change > increase[1]:
            increase[0] = row[0]
            increase[1] = net_change

        # Calculate the greatest decrease
        if net_change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_change

# Calculate the average net change
avg_change = sum(net_change_list) / len(net_change_list)

# Generate the output
summary = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n"
)

# Print the output
print(summary)

# Write the results to a text file
with open(file_to_output, "w") as txt:
    txt.write(summary)
