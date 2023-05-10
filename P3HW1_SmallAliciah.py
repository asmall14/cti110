# 4/20/2023

# P3HW1_DeBugging

# Aliciah Small


# This program takes a number grade, determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average for grades

low = min(grades)
high = max(grades)
sum1 = sum(grades)
avg = sum(grades)/6

# determine low, high, sum1, and avg of input grades

print(f"\n------------Results------------")
print(f'{"Lowest Grade: ":<21}{low:<21}')
print(f'{"Highest Grade: ":<21}{high:<21}')
print(f'{"Sum of Grades: ":<21}{sum1:<21}')
print(f'{"Average: ":<21}{avg:.2f}')

print("-------------------------------")

# determine letter grade for avg


if avg >= 90:
  print('Your grade is: A')
else:
 if avg >= 80:
   print('Your grade is: B')
 else:
  if avg >= 70:
    print('Your grade is: C')
  else:
   if avg >= 60:
     print('Your grade is: D')
   else:
    if avg < 60:
      print('Your grade is: F')





