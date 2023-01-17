import os
import csv 


# inform path to collect data from 

election_data = os.path.join ('..', 'Resources', 'election_data.csv')

# define lists to store data

voters_list = []
candidates_list = []


# read csv file

with open (election_data, "r", encoding="utf-8") as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=",")

    # print(csvreader)

    csv_header = next (csvreader)


    for row in csvreader:
        # print(row)

        voters_list.append(row[0])
        candidates_list.append(row[2])


election = dict()
# voters = dict()
# candidates = dict()

election = {"Voters":voters_list, "Candidates":candidates_list}

print(f'Total votes: {len(election["Voters"])}') # 



election["Candidates"] = candidates_list

unique_candidates = set(candidates_list)
candidates = list(unique_candidates)
# print(candidates)

candidate_1 = (candidates[0])

candidate_2 = (candidates[1])

candidate_3 = (candidates[2])



# candidate_1_votes = []
# for candidates in candidates_list:
#     if candidates == candidate_1:
#         candidate_1_votes.append(candidates)
# candidate_1_votes = (len(candidate_1_votes))
# print(f'{candidate_1}: {candidate_1_votes}')


candidate_1_votes = []
candidate_2_votes = []
candidate_3_votes = []


for candidates in candidates_list:
    if candidates == candidate_1:
        candidate_1_votes.append(candidates)
    if candidates == candidate_2:
        candidate_2_votes.append(candidates)
    if candidates == candidate_3:
        candidate_3_votes.append(candidates)


candidate_1_votes = (len(candidate_1_votes))
candidate_2_votes = (len(candidate_2_votes))
candidate_3_votes = (len(candidate_3_votes))

print(f'{candidate_1}: {candidate_1_votes}')
print(f'{candidate_2}: {candidate_2_votes}')
print(f'{candidate_3}: {candidate_3_votes}')



# votes_candidate_1 = (candidates.count("Charles Casper Stockham"))
# charles_percentage = ((int(votes_charles) * 100)/ int(len(voters)))
# print(f"Charles Casper Stockham: {(round(charles_percentage,3))} % ({votes_charles})")




# charles_percentage = ((int(votes_charles) * 100)/ int(len(voters)))
# print(f"Charles Casper Stockham: {(round(charles_percentage,3))} % ({votes_charles})")














# print(f'Total votes: '[total_votes])

















