# python-challenge
In this challenge we will be using two files one is for the election data in which we will be determining the winner and the insights of the election and the other one is the financial record of a company which comprises of profit and loss statement.
Through the profit and loss csv (Budget csv) file we will determine the total number of months, the net total, the average change, the greatest increase in profit and the greatest decrease in profit in the data set
Through the election data csv file we will write a python script which will determine the total number of votes casted, the total number of votes each candidate won, the winner of the election.

These are the codes which I have used
Election.

import os
import csv
#Objective 1: Importing the CSV file for Analysis
pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)
csvpath = os.path.join(pwd,"Resources","election_data.csv")
txtfile= os.path.join(pwd,"Analysis","output.txt")
dir="Analysis"
p_dir="python-challenge"
path=os.path.join(p_dir,dir)
print(csvpath)
# Objective 2: Create the lists to store data. Initialize

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

# Open the CSV using the set path PyPollcsv

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Conduct the ask
    for row in csvreader:
        # Count the total number of votes
        count = count + 1
        # Set the candidate names to candidatelist
        candidatelist.append(row[2])
        # Create a set from the candidatelist to get the unique candidate names
    for x in set(candidatelist):
        unique_candidate.append(x)
        # y is the total number of votes per candidate
        y = candidatelist.count(x)
        vote_count.append(y)
        # z is the percent of total votes per candidate
        z = (y/count)*100
        vote_percent.append(z)
       
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    

# Print to terminal
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 
 
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt
# Output perhaps needs to be rounded to 3 decimal points. Leaving that formatting out for now) 

with open('election_results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(unique_candidate))):
        text.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("The winner is: " + winner + "\n")
    text.write("---------------------------------------\n")

# Specify the path where you want to save the file
file_path = "C:/Users/DELL/Documents/Data_Bootcamp/Homework/python_challenge/python-challenge/election_results.txt"

# Open the file in write mode ('w') or append mode ('a')
# If the file doesn't exist, 'w' mode will create it; if it exists, it will overwrite its content
# If you want to append to an existing file, use 'a' mode instead of 'w'
with open(file_path, 'r') as file, open('C:/Users/DELL/Documents/Data_Bootcamp/Homework/python_challenge/python-challenge/PyPoll/Analysis/election_results.txt','a') as file2:
    for line in file:
         file2.write(line)

Budget one         
import os
import csv
# Objective 1: Opening the Csv file for the analysis
pwf = os.path.abspath(__file__)
pwd = os.path.dirname(pwf)
csvpath = os.path.join(pwd,"Resources","budget_data.csv")
# Objective 2: Create the lists to store data. Initialize
 

profit = []
monthly_changes = []
date = []

# Initialize the variables as required.
 
count = 0
total_profit = 0
total_change_profits = 0
# initial_profit = 0

# Open the CSV using the set path PyBankcsv

with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        csv_header = next(csvreader)
        first_row=next(csvreader)
        initial_profit=int(first_row[1])
        total_profit+=int(first_row[1])
        # Use count to count the number months in this dataset
        count = count + 1
        # Conducting the ask
        for row in csvreader:    
          # Use count to count the number months in this dataset
          count = count + 1 

          # Will need it when collecting the greatest increase and decrease in profits
          date.append(row[0])

          # Append the profit information & calculate the total profit
          profit.append(row[1])
          total_profit = total_profit + int(row[1])

          #Calculate the average change in profits from month to month. Then calulate the average change in profits
          final_profit = int(row[1])
          monthly_change_profits = final_profit - initial_profit
          initial_profit = int(row[1])
          #Store these monthly changes in a list
          monthly_changes += [monthly_change_profits]     

          total_change_profits = total_change_profits + monthly_change_profits
          initial_profit = final_profit

          
          
          
          #Find the max and min change in profits and the corresponding dates these changes were obeserved
          greatest_increase_profits = max(monthly_changes)
          greatest_decrease_profits = min(monthly_changes)

          increase_date = date[monthly_changes.index(greatest_increase_profits)]
          decrease_date = date[monthly_changes.index(greatest_decrease_profits)]
#Calculate the average change in profits
average_change_profits = sum(monthly_changes)/len(monthly_changes)
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: $" + f"{average_change_profits:.2f}")
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
print("----------------------------------------------------------")

with open('financial_analysis.txt', 'w') as text:
        text.write("----------------------------------------------------------\n")
        text.write("  Financial Analysis"+ "\n")
        text.write("----------------------------------------------------------\n\n")
        text.write("    Total Months: " + str(count) + "\n")
        text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
        text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
        text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
        text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
        text.write("----------------------------------------------------------\n")
# Specify the path where you want to save the file
file_path = "C:/Users/DELL/Documents/Data_Bootcamp/Homework/python_challenge/python-challenge/financial_analysis.txt"

# Open the file in write mode ('w') or append mode ('a')
# If the file doesn't exist, 'w' mode will create it; if it exists, it will overwrite its content
# If you want to append to an existing file, use 'a' mode instead of 'w'
with open(file_path, 'r') as file, open('C:/Users/DELL/Documents/Data_Bootcamp/Homework/python_challenge/python-challenge/PyBank/Analysis/financial_analysis.txt','a') as file2:
    for line in file:
         file2.write(line)
