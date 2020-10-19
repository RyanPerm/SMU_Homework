# Dependencies
import os
import csv

filepath = r"Instructions\PyPoll\Resources\election_data.csv"

totalVote = 0

candidateDict = {}

with open(filepath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(f"CSV Header: {header}")


    for row in csvreader:

        totalVote += 1

        #voter_ID = [0]
        #county = [1]
        candidate = row[2]
        if candidate in candidateDict.keys():
            candidateDict[candidate] += 1
        else:
            candidateDict[candidate] = 1

# print(f"Correy Vote: {correy_count}, Khan Vote: {khan_count}, LI Vote: {li_count}, O'Tooley Vote: {otooley_count},")

winner = max(candidateDict, key=candidateDict.get)

percentDict = {}
for key in candidateDict.keys():
    percent = candidateDict[key] / totalVote
    percentDict[key] = percent

print (percentDict)

stringsDict = []
for key in percentDict.keys():
    string = key + ": " + str(round(percentDict[key]* 100, 3)) + "% (" + str(candidateDict[key]) + ")"
    stringsDict.append(string)

print(stringsDict)

finalString = "\n".join(stringsDict)

summaryString = f"""Election Results
-------------------------
Total Votes: {totalVote}
-------------------------
{finalString}
-------------------------
Winner: {winner}
-------------------------"""


with open("pypoll_result.txt", "w") as file1:
    file1.write(summaryString)