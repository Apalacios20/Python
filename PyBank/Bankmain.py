import os
import csv

csvpath = os.path.join("..", "Python-Challenge", "PyBank", "Resources", "budgetdata.csv")
   
date = []
total_profit = []
profit_change = []

with open(csvpath, 'r') as file_handler:
    csv_reader = csv.reader(file_handler, delimiter=",")
    csv_header = next(file_handler)
   
    for row in csv_reader:
        date.append(row[0])
        total_profit.append(int(row[1]))    
     
    for i in range(len(total_profit)-1):
        profit_change.append(total_profit[i+1]-total_profit[i])

average_profit_change = round(sum(profit_change)/ len(profit_change),2)
maximum = max(profit_change)
minimum = min(profit_change)
date_maximum = date[profit_change.index(maximum)+1]
date_minimum = date[profit_change.index(minimum)+1]


print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {average_profit_change}")
print(f"Greatest Increase in Profits: {date_maximum} (${(str(maximum))})")
print(f"Greatest Decrease in Profits: {date_minimum} (${(str(minimum))})")

csvpath2 = os.path.join("..","Python-Challenge","PyBank","Financial_Analysis_Summary.txt")

with open(csvpath2, "w", newline = "") as text:
    text.write("\n")
    text.write("Financial Analysis\n")
    text.write("------------------------\n")
    text.write(f"Total Months: {len(date)}\n")
    text.write(f"Total: ${sum(total_profit)}\n")
    text.write(f"Average Change: ${average_profit_change}\n")
    text.write(f"Greatest Increase in Profits: {date_maximum} (${maximum})\n")
    text.write(f"Greatest Decrease in Profits: {date_minimum} (${minimum})\n")