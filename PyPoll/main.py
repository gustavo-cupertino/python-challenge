# import modules 

import os
import csv 

# inform path to collect data from 

election_data = os.path.join ('..', 'Resources', 'election_data.csv')

# define lists to store data

voters = []
candidates = []
unique_candidates = []

# read csv file

with open (election_data, "r", encoding="utf-8") as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=",")

# store header

    csv_header = next (csvreader)

# print rows and add values to the lists 

    for row in csvreader:

        voters.append(row[0])
        candidates.append(row[2])

# printing report to terminal

print("Elections Results")

print("----------------------------------------")

# total number of votes cast

print(f"Total votes: {(len(voters))}")

print("----------------------------------------")

# finding candidates list with unique values 

unique_candidates.append(set(candidates))
candidate_list = []
candidate_list = list(unique_candidates)
#print(candidate_list)

# printing total of votes and percentage for each candidate 

votes_charles = (candidates.count("Charles Casper Stockham"))
charles_percentage = ((int(votes_charles) * 100)/ int(len(voters)))
print(f"Charles Casper Stockham: {(round(charles_percentage,3))} % ({votes_charles})")


votes_raymon = (candidates.count("Raymon Anthony Doane"))
raymon_percentage = ((int(votes_raymon) * 100)/ int(len(voters)))
print(f"Raymon Anthony Doane: {(round(raymon_percentage,3))} % ({votes_raymon})")


votes_diana = (candidates.count("Diana DeGette"))
diana_percentage = ((int(votes_diana) * 100)/ int(len(voters)))
print(f"Diana DeGette: {(round(diana_percentage,3))} % ({votes_diana})")

print("----------------------------------------")

# printing the election's winner

if votes_charles > votes_raymon and votes_charles > votes_diana:
    print("Winner: Charles Casper Stockham")
elif votes_raymon > votes_charles and votes_raymon > votes_diana:
    print("Winner: Raymon Anthony Doane")
else:
    print("Winner: Diana DeGette")

print("----------------------------------------")


# exporting report as a text file


output_file = os.path.join('..', 'Analysis', 'election_analysis.txt')


with open(output_file, 'w') as text_file:
    writer = csv.writer(text_file)


    print("Elections Results", file=text_file)

    print("----------------------------------------", file=text_file)

    print(f"Total votes: {(len(voters))}", file=text_file)

    print("----------------------------------------", file=text_file)

    print(f"Charles Casper Stockham: {(round(charles_percentage,3))} % ({votes_charles})", file=text_file)
    print(f"Raymon Anthony Doane: {(round(raymon_percentage,3))} % ({votes_raymon})", file=text_file)
    print(f"Diana DeGette: {(round(diana_percentage,3))} % ({votes_diana})", file=text_file)

    print("----------------------------------------", file=text_file)

    if votes_charles > votes_raymon and votes_charles > votes_diana:
        print("Winner: Charles Casper Stockham", file=text_file)
    elif votes_raymon > votes_charles and votes_raymon > votes_diana:
        print("Winner: Raymon Anthony Doane", file=text_file)
    else:
        print("Winner: Diana DeGette", file=text_file)

    print("----------------------------------------", file=text_file)
