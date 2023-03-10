# importing modules

import os
import csv

# inform path to collect data from 

budget_data = os.path.join ('..', 'Resources', 'budget_data.csv')

# define lists to store data

months = []
results = []
result_change = []

# read csv file

with open (budget_data, "r", encoding="utf-8") as csvfile:
    
    csvreader = csv.reader(csvfile,delimiter=",")


# store header

    csv_header = next (csvreader)


# printing values to lists

    for row in csvreader:

        months.append(row[0])
        results.append(int(row[1]))
              
    
# printing report to terminal


print("Financial Analysis")

print("----------------------------------------------------")

# Total of months 

print(f"Total months: {len(months)}")

# net total amount over period 
   
print(f"Total amount of Profit/Losses: ${sum(results)}")

# Finding the changes in "profit / losses" over the period 

for x in range(len(results) - 1):
    result_change.append(results[x+1] - results[x])

total_changes = sum(result_change)

# Printing the average of changes in "profit / losses" over the period     

average_change = (((total_changes)/(len(months)-1)))
rounded_average = round(average_change,2)
print(f"Average Change: ${rounded_average}")

# Printing the greatest increase / decrease over the entire period

greatest_increase = (max(result_change))
greatest_month = (months[(result_change.index(max(result_change)))+1])
print(f"Greatest increase in Profits: {greatest_month} (${(greatest_increase)})")


greatest_decrease = (min(result_change))
worst_month = (months[(result_change.index(min(result_change)))+1])
print(f"Greatest decrease in Profits: {worst_month} (${(greatest_decrease)})")

# Exporting report to a text file 

output_file = os.path.join('..', 'Analysis', 'budget_analysis.txt')


with open(output_file, 'w') as text_file:
    writer = csv.writer(text_file)


    print("Financial Analysis" , file=text_file)

    print("----------------------------------------------------", file=text_file)

    print(f"Total months: {len(months)}", file=text_file)

    print(f"Total amount of Profit/Losses: ${sum(results)}", file=text_file)

    print(f"Average Change: ${rounded_average}", file=text_file)

    print(f"Greatest increase in Profits: {greatest_month} (${(greatest_increase)})", file=text_file)

    print(f"Greatest decrease in Profits: {worst_month} (${(greatest_decrease)})", file=text_file)

