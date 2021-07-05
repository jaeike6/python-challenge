# Header of the financial report
print("Financial analysis")
print("---------------------------------------------------")

# Read CSV file
import os
import csv

date = []
profit_loss =[]

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])
# print (date)
# print (profit_loss)

# The total number of months included in the dataset
number_of_month = len(date)
print(f"Total months : {number_of_month}")

# The net total amount of "Profit/Losses" over the entire period
total =0
int_proift_loss = [int(number) for number in profit_loss]
# print(int_proift_loss)

for element in range(0,len(int_proift_loss)) :
    total = total + int_proift_loss[element]
print("Total : $", total)

# The average of the changes in "Profit/Losses" over the entire period

difference = []

for x, y in zip(int_proift_loss[0::], int_proift_loss[1::]):
    difference.append(y-x)
# print ("Average  Change : ", str(difference))

average = sum(difference) / len(difference)
print("Average  Change: $" + str(round(average, 2)))

# The greatest increase in profits (date and amount) over the entire period

date.remove('Jan-10')                    # remove Jan-10 to correct matching between the date and difference
# print(date)

max = max(difference)
# print(max)                               #1926159
# print(difference.index(max))             #24
# print(date[difference.index(max)])       #Feb-12

print (f"Greatest Increase in Profits: {date[difference.index(max)]} (${max})")

# The greatest decrease in losses (date and amount) over the entire period

min = min(difference)
# print(min)                               #-2196167
# print(difference.index(min))             #43
# print(date[difference.index(min)])       #Sep-13

print (f"Greatest Decrease in Profits: {date[difference.index(min)]} (${min})") 
  
# write text file

file ='../Analysis/financial analysis.txt'
with open(file, 'w') as result:
    result.writelines("financial analysis")
    result.write('\n')
    result.writelines("--------------------------")
    result.write('\n')
    result.writelines((f"Total months : {number_of_month}"))
    result.write('\n')
    result.writelines(f"Total : $ {total}")
    result.write('\n')
    result.writelines("Average  Change: $" + str(round(average, 2)))
    result.write('\n')
    result.writelines(f"Greatest Increase in Profits: {date[difference.index(max)]} (${max})")
    result.write('\n')
    result.writelines(f"Greatest Decrease in Profits: {date[difference.index(min)]} (${min})")

# end