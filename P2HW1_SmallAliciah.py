
# This program asks user to input 4 numbers to determine travel expenses and to list destination

# 4/7/23

# CTI-110 P2HW1 - Travel

# Aliciah Small

#

print("This program calculates and displays travel expenses")

print()

num1 = float( input("Enter Budget: "))

print()

loc = input("Enter your travel destination: ")

print ()

num2 = float( input("How much do you think you will spend on gas? "))

print ()

num3 = float( input("Approximately, how much will you need for accomodation/hotel? "))

print ()

num4 = float( input("Last, how much do you need for food? "))

print ()

print("------------Travel Expenses------------")

print(f'{"Location: ":<21}{loc}')

print(f'{"Initial Budget: ":<20} ${num1}')

print(f'{"Fuel: ":<20} ${num2}')

print(f'{"Accomodation: ":<20} ${num3}')

print(f'{"Food: ":<20} ${num4}')

print("---------------------------------------")

print()

# Program adds the numbers

total = num2 + num3 + num4

bal = num1 - total

# Results are displayed

print(f'{"Remaining Balance: ":<20} ${bal}')
