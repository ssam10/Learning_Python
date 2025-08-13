# Tip Calculator Project
# Day 2
# Author : Samridhi [04-07-2025]

print("Welcome to Tip Calculator!")
#what wa sthe total bill
# how much tip woul dyou like to give 10, 12 or 15
# how many people to split the bill?
# Display Each person has to pay
bill = float(input("What is the total bill?\n"))
tip_percent = int(input("How much tip would you like to give? 10, 12 or 15?\n"))
n_people = int(input("How many people to split the bill?\n"))
total_bill = bill + (bill * tip_percent/100)
Per_person_amt = round(total_bill/n_people,2)
print(f"Each person has to pay: {Per_person_amt}")