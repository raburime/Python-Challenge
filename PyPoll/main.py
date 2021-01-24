# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

#filepath = '..\Resources\Accounting.csv'
csvpath = os.path.join("..", "Resources", 'election_data.csv')
print("csvpath.. " + csvpath)



with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')


    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    print(csvreader)
    total_number_of_votes_cast = 0
    Khan_count = 0
    Correy_count = 0
    Li_count = 0
    Other_count = 0
    OTooley_count = 0
    
    
    # Read each row of data after the header
    for row in csvreader:
            voterID = str(row[0])
            county = str(row[1])
            candidate = str(row[2])
            total_number_of_votes_cast += 1
            if candidate == 'Khan':
                Khan_count += 1
            elif (candidate == 'Correy'):
                Correy_count += 1
            elif (candidate == 'Li'):
                Li_count += 1
            elif (candidate == "O'Tooley"):
                OTooley_count += 1
            else:
                Other_count += 1
                print("Other Candidate: " + row[2])
   
        
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_number_of_votes_cast))
    print("-------------------------")
    Khan_percentage = (Khan_count/total_number_of_votes_cast) * 100
    Li_percentage = (Li_count/total_number_of_votes_cast) * 100
    OTooley_percentage = (OTooley_count/total_number_of_votes_cast) * 100
    Correy_percentage = (Correy_count/total_number_of_votes_cast) * 100
    if (Khan_count > Li_count) and (Khan_count > OTooley_count) and (Khan_count > Correy_count):
        winner = 'Khan'
    elif (Li_count > OTooley_count) and (Li_count > Khan_count) and (Li_count > Correy_count):
        winner = 'Li'
    elif (Correy_count > OTooley_count) and (Correy_count > Khan_count) and (Correy_count > Li_count):
        winner = 'Correy'
    elif (OTooley_count > Li_count) and (OTooley_count > Khan_count) and (OTooley_count > Correy_count):
        winner = "O'Tooley"
        
    print("Khan: " + str(Khan_percentage) + "%" + " " + "(" + str(Khan_count) + ")")
    print("Correy: " + str(Correy_percentage) + "%" + " " + "(" + str(Correy_count) + ")")
    print("Li: " + str(Li_percentage) + "%" + " " + "(" + str(Li_count) + ")")
    print("O'Tooley: " + str(OTooley_percentage) + "%" + " " + "(" + str(OTooley_count) + ")")
    print("-------------------------")
    print("Winner: " + str(winner))
    print("-------------------------")


