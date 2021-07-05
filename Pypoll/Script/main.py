# Header of Election report
print("Election Results")
print("---------------------------------------------------")

# Read CSV file
import os
import csv

voter_ID = []
county =[]
candidate =[]

csvpath = os.path.join('..', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    for row in csvreader:
        voter_ID.append(row[0])
        county.append(row[1])
        candidate.append(row[2])
# print (voter_ID)                     # do no run if you cannot wait
# print (county)                       # do no run if you cannot wait
# print (candidate)                    # do no run if you cannot wait

# The total number of votes cast
total_votes = len(voter_ID)
print(f"Total Votes : {total_votes}")
print("---------------------------------------------------")

# Candidate name / percent / # of votes

Khan_count = candidate.count("Khan")
Khan_portion = Khan_count/total_votes
Khan_percentage = "{:.3%}".format(Khan_portion)
print(f"Khan: {Khan_percentage} ({Khan_count})")

Correy_count = candidate.count("Correy")
Correy_portion = Correy_count/total_votes
Correy_percentage = "{:.3%}".format(Correy_portion)
print(f"Correy: {Correy_percentage} ({Correy_count})")

Li_count = candidate.count("Li")
Li_portion = Li_count/total_votes
Li_percentage = "{:.3%}".format(Li_portion)
print(f"Li: {Li_percentage} ({Li_count})")

Tooley_count = candidate.count("O'Tooley")
Tooley_portion = Tooley_count/total_votes
Tooley_percentage = "{:.3%}".format(Tooley_portion)
print(f"O'Tooley: {Tooley_percentage} ({Tooley_count})")

print("---------------------------------------------------")

# Choose final winner

election = {Khan_count:"Khan", Correy_count:"Correy", Li_count : "Li", Tooley_count : "O'Tooley"}

print(f'Winner : {election[max(Khan_count,Correy_count,Li_count,Tooley_count)]}')

print("---------------------------------------------------")

file ='../Analysis/Election result.txt'
with open(file, 'w') as result:
    result.writelines("Election Results")
    result.write('\n')
    result.writelines("---------------------------------------------------")
    result.write('\n')
    result.writelines((f"Total Votes : {total_votes}"))
    result.write('\n')
    result.writelines("---------------------------------------------------")
    result.write('\n')
    result.writelines(f"Khan: {Khan_percentage} ({Khan_count})")
    result.write('\n')
    result.writelines(f"Correy: {Correy_percentage} ({Correy_count})")
    result.write('\n') 
    result.writelines(f"Li: {Li_percentage} ({Li_count})")
    result.write('\n') 
    result.writelines(f"O'Tooley: {Tooley_percentage} ({Tooley_count})")
    result.write('\n') 
    result.writelines("---------------------------------------------------")
    result.write('\n')
    result.writelines(f'Winner : {election[max(Khan_count,Correy_count,Li_count,Tooley_count)]}')
    result.write('\n')
    result.writelines("---------------------------------------------------")
    
