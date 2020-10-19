import csv


filepath = r"Instructions\PyBank\Resources\budget_data.csv"

totalMonths = 0
totalProfit = 0

firstRow = True
prevRow = 0
changeDict = {}

with open(filepath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(f"CSV Header: {header}")


    for row in csvreader:
        #month-year = row[0]
        #profit/loss = row[1]

        totalMonths += 1
        totalProfit += int(row[1])

        if firstRow:
            prevRow = int(row[1])
            firstRow = False
        else:
            change = int(row[1]) - prevRow
            changeDict[row[0]] = change
            prevRow = int(row[1])

averageChange = sum(changeDict.values()) / len(changeDict)

maxChange = max(changeDict, key=changeDict.get)
maxChangeVal = changeDict[maxChange]

minChange = min(changeDict, key=changeDict.get)
minChangeVal = changeDict[minChange]

summaryString = f"""Finanical Analysis
-------------------------
Total Months: {totalMonths}
Total: ${totalProfit}
Average Change: ${round(averageChange, 2)}
Greatest Increase in Profits: {maxChange} (${maxChangeVal})
Greatest Decrease in Profits: {minChange} (${minChangeVal})
"""

with open("pybank_result.txt", "w") as file1:
    file1.write(summaryString)