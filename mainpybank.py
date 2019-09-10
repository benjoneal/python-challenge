# PyBank
import os
import csv

budget_data = os.path.join("budget_data.csv")

def AvgMonth(Month):
    total = 0

    for i in Month:
        total += int(i)

    Ave = total/len(Month)
    return Ave


with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile, None)

    
    Months = []

    TotalDollars = 0
    Monthbymonth = []
    PreviousMonthProfit = 0
    BigGain = 0
    BigLoss = 0

    for row in csvreader: 
        Months.append(row[0])
        TotalDollars += int(row[1])
        Monthbymonth.append(int(row[1])-PreviousMonthProfit)
        PrevousMonthProfit = int(row[1])

        if int(row[1]) > BigGain:
                BigGain = int(row[1])
                GainMonth = row[0]

        if int(row[1])< BigLoss:
            BigLoss = int(row[1])
            LossMonth = row[0]


    
#Output

    print("Financial Analysis")
    print("-------------------")
    print(f"Months:{len(Months)}")
    print(f"Total Profits: ${TotalDollars}")
    print(f"Average Monthly Profit: ${round(AvgMonth(Monthbymonth),2)}")
    print(f"Largest Profit Month: {GainMonth}; Profit: ${BigGain}")
    print(f"Largest Loss Month: {LossMonth}; Profit: ${BigLoss}")

    f= open("Bank.txt","w+")
    f.write("Financial Analysis" "\n")
    f.write("-------------------" "\n")
    f.write(f"Months:{len(Months)}" "\n")
    f.write(f"Total Profits: ${TotalDollars}" "\n")
    f.write(f"Average Monthly Profit: ${round(AvgMonth(Monthbymonth),2)}" "\n")
    f.write(f"Largest Profit Month: {GainMonth}; Profit: ${BigGain}" "\n")
    f.write(f"Largest Loss Month: {LossMonth}; Profit: ${BigLoss}" "\n")
    f.close