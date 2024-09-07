
# Python Challenge: PyBank and PyPoll

## Overview

This repository contains two Python scripts created for the Python challenge: **PyBank** and **PyPoll**. These scripts use Python to analyze large datasets, showcasing how programming can replace Excel for more efficient data processing.

## Repository Structure

- `PyBank/` - Contains the Python script and analysis for the PyBank financial records challenge.
  - `main.py` - The Python script that performs the analysis.
  - `Resources/` - Folder containing the dataset used for analysis.
  - `analysis/` - Folder containing the output text file with the analysis results.
  
- `PyPoll/` - Contains the Python script and analysis for the PyPoll election results challenge.
  - `main.py` - The Python script that performs the analysis.
  - `Resources/` - Folder containing the dataset used for analysis.
  - `analysis/` - Folder containing the output text file with the analysis results.

## PyBank Challenge

### Objective:
Analyze the financial records in the dataset `budget_data.csv` to calculate:
- Total number of months.
- Total profit/loss.
- Average change in profit/loss between months.
- The greatest increase in profits.
- The greatest decrease in profits.

### Script Details:
- The script reads data from the `Resources/budget_data.csv` file.
- It calculates the total number of months, total profit/loss, and the average change in profits.
- The greatest increase and decrease in profits are also identified.
- The results are both printed to the terminal and exported to `analysis/PyBank Analysis.txt`.

### Example Output:
```
Financial Analysis
------------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)
```

## PyPoll Challenge

### Objective:
Analyze election data in the dataset `election_data.csv` to determine:
- The total number of votes.
- The percentage and number of votes each candidate received.
- The winner of the election based on popular vote.

### Script Details:
- The script reads data from the `Resources/election_data.csv` file.
- It calculates the total votes cast, each candidate's vote count, and percentage of votes.
- The winner is determined based on the highest number of votes.
- The results are both printed to the terminal and exported to `analysis/PyPoll Analysis.txt`.

### Example Output:
```
Election Results
--------------------------
Total Votes: 369711
--------------------------
Charles Casper Stockham: 23.05% (85213)
Diana DeGette: 73.81% (272892)
Raymon Anthony Doane: 3.14% (11606)
--------------------------
Winner: Diana DeGette
```

## Requirements

The scripts should:
- Read in the CSV files correctly.
- Print results to the terminal.
- Export results to a text file.
- Run error-free with consistent results.
- Have clean and commented code.

## Usage

1. Clone the repository:
    ```
   git clone https://github.com/the-eva-a/python-challenge.git
   ```

2. Navigate to either `PyBank` or `PyPoll` folders and run the script:
   
   ```
   python main.py
   ```

## Acknowledgements

This project is part of the curriculum in the edX Data Analytics Bootcamp. Special thanks to my instructors and peers for their support and guidance.

