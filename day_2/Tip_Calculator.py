#!/usr/bin/python3
print("Welcome to the tip calculator.")
print("===================================")
bill = float(input("what was the total bill? $"))
valid_percentages = [0, 10, 12, 15]
percent = -1
while percent not in valid_percentages:
    percent = int(input(
        "what percentage tip would you like to give? 10,12,15? "))
    if percent not in valid_percentages:
        print("wrong percentage")
        print("choose from (0, 10, 12, 15)")
total_tip = bill * (percent / 100)
total_must_pay = total_tip + bill
num_of_persons = int(input("How many people to split the bill? "))
print("Each person should pay: {:.2f}".format(total_must_pay / num_of_persons))
