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
        z_formatted = "{:.3f}".format(z)
        vote_percent.append(z_formatted)
       
        
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
