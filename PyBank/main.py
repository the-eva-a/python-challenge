import csv

budget_data = []
# Open the budget_data file
with open('PyBank/Resources/budget_data.csv', mode='r', newline='') as file:
    readit = csv.reader(file)
    next(readit) # Skip the header
    for row in readit:
        row[1] = int(row[1]) # Convert string to integer
        budget_data.append(row) # Add budget data to the budget_data array


# Total months is all entries minus the header
total_months = len(budget_data)

# Calculate the total profit / loss
total = 0
monthly_change = {}
for i in range(0, len(budget_data)):
    total += budget_data[i][1]
    if i > 0:
        # calculate the change in profit/loss between months 
        monthly_change[budget_data[i][0]] = budget_data[i][1] - budget_data[i-1][1]
changes = list(monthly_change.values())

if changes:
    avg_change = round(sum(changes) / len(changes),2)
else: 
    avg_change = 0
max_gain = max(changes)
max_gain_month = [month for month, change in monthly_change.items() if change == max_gain][0]
max_loss = min(changes)
max_loss_month = [month for month, change in monthly_change.items() if change == max_loss][0]

results = (f"Financial Analysis\n"
           "------------------------------\n"
           f"Total Months: {total_months}\n"
           f"Total: ${total}\n"
           f"Average Change: ${avg_change}\n"
           f"Greatest Increase in Profits: {max_gain_month} (${max_gain})\n"
           f"Greatest Decrease in Profits: {max_loss_month} (${max_loss})\n")


# Output the Financial Analysis Statement
print(results)

with open("PyBank/analysis/PyBank Analysis.txt", "w") as f:
    f.write(results)
