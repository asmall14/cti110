
# This program asks user to input 4 numbers to determine travel expenses and to list destination

# 4/5/23

# CTI-110 P1HW1 - Travel Expense

# Aliciah Small 

#

print("This program calculates and displays travel expenses")

print()

num1 = int( input("Enter Budget: "))

print()

loc = input("Enter your travel destination: ")

print ()

num2 = int( input("How much do you think you will spend on gas? "))

print ()

num3 = int( input("Approximately, how much will you need for accomodation/hotel? "))

print ()

num4 = int( input("Last, how much do you need for food? "))

print ()

print("------------Travel Expenses------------")

print("Location: ",loc)

print("Initial Budget: ",num1)

print()

print("Fuel: ",num2)

print("Accomodation: ",num3)

print("Food: ",num4)

print()

# Program adds the numbers

total = num2 + num3 + num4

bal = num1 - total

# Results are displayed

print("Remaining Balance: ",bal)
