import os
import csv

# Set path for file
budget_tracker = os.path.join("..", "python-challenge0", "Resources_CSV", "budget_data.csv")

# make lists to store the data
total_months = []
total_profit = []
monthtomonth_change = []

# opening the CSV
with open(budget_tracker) as csvfile:
    reader = csv.reader(csvfile)

    # Read the header row first
    header = next(reader)

    # Read through each row of data after the header
    for row in reader: 

        # Find total months
        total_months.append(row[0])

        # Find total profit
        total_profit.append(int(row[1])) 

    # Find average change
    for i in range(len(total_profit)-1):
        monthtomonth_change.append(total_profit[i+1]-total_profit[i])

    # Find max and min profit values
    maxvalue_increase = max(monthtomonth_change)
    maxvalue_decrease = min(monthtomonth_change)

    # Find proper month for max and min values
    maxmonth_increase = monthtomonth_change.index(max(monthtomonth_change)) + 1
    maxmonth_decrease = monthtomonth_change.index(min(monthtomonth_change)) + 1

    # Print Statements
    print("Financial Analysis")
    print("-----------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(total_profit)}")
    print(f"Average Change: {sum(monthtomonth_change)/len(monthtomonth_change)}")
    print(f"Greatest Increase in Profits: {total_months[maxmonth_increase]} (${(str(maxvalue_increase))})")
    print(f"Greatest Decrease in Profits: {total_months[maxmonth_decrease]} (${(str(maxvalue_decrease))})")

    # Export text file 
    output_pybankfile = os.path.join("..", "python-challenge0", "Resources_CSV", "PyBank_Mod3.txt")
    with open(output_pybankfile, "w") as file:
        file.write("Financial Analysis")
        file.write("-----------------------")
        file.write(f"Total Months: {len(total_months)}")
        file.write(f"Total: ${sum(total_profit)}")
        file.write(f"Average Change: {sum(monthtomonth_change)/len(monthtomonth_change)}")
        file.write(f"Greatest Increase in Profits: {total_months[maxmonth_increase]} (${(str(maxvalue_increase))})")
        file.write(f"Greatest Decrease in Profits: {total_months[maxmonth_decrease]} (${(str(maxvalue_decrease))})")
        
    







