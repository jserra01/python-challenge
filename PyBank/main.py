# PyBank: Module 3 Challange - Financial Analysis

# Calculate: Total Months, Total Profit/Loss, Total Change in Profit/Loss, Avg Change in Profit/Loss, Greatest increase and decrease in profit (and month)

#Import csv file.  Comma delimited with Date (MMM-YY) and Profit/Loss (int with positive & negative values)
import os
import csv

csvpath = os.path.join(".", "Resources", "budget_data.csv")

#Set file to write output
file = "./analysis/financial_analysis.txt"

#Set variables for calculations 
months = 0
profit_loss = 0
p_l_month = []
p_l_amnt = []
total_chg_p_l = 0
avg_p_l_chg = 0
max_increase = 0
max_decrease = 0
last_month_p_l = 0

#Use csv file.
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ",")

    csvheader = next(csvreader)

    for row in csvreader:
        # Calculate Total Months
        months += 1

        # Calculate Total Profit/Loss
        profit_loss += int(row[1])

        # write month and profit_loss from previous month
        if months > 1:
            p_l_month.append(row[0])
            p_l_amnt.append(int(row[1]) - last_month_p_l)

        # store current month p_l (for use in calculating previous month)
        last_month_p_l = int(row[1])
csvfile.close()

#Calculate Total Change in Profit/Loss
for x in range(0, len(p_l_amnt)):
    total_chg_p_l += p_l_amnt[x]

#Calculate Average Change in Profit/Loss
avg_p_l_chg = round(total_chg_p_l/len(p_l_amnt),2)

#Calculate Max Increase and Decrease
max_increase = max(p_l_amnt)
max_inc_index = p_l_amnt.index(max_increase)
max_increase_month = p_l_month[max_inc_index]

max_decrease = min(p_l_amnt)
max_dec_index = p_l_amnt.index(max_decrease)
max_decrease_month = p_l_month[max_dec_index]

#Write and Print Results
header1 = "Financial Analysis"
header2 = "------------------------------"

results = [f'{header1}\n',
           f'{header2}\n',
           f'Total Months: {months}\n',
           f'Total: ${profit_loss}\n',
           f'Average Change: ${avg_p_l_chg}\n'
           f'Greatest Increase in Profits: {max_increase_month} (${max_increase})\n'
           f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})'
]

with open(file, "w") as text:
    text.writelines(results)
text.close()

print(f'{header1}\n{header2}\n')
print(f'Total Months: {months}\n')
print(f'Total: ${profit_loss}\n')
print(f'Average Change: ${avg_p_l_chg}\n')
print(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})\n')
print(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})')