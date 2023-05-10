# CTI 110

# P3HW2_Salary

# Aliciah Small

# 4/20/2023

# This program determines employee pay.

# Employee information input here

emp_name = input('Enter employee\'s name: ')
hrs_worked = float(input('Enter number of hours worked: '))
pay_rate = float(input('Enter employee\'s pay rate: '))

print(f"------------------------------------------")

print('Employee name: ', emp_name)

print()

# Determine overtime amt, overtime pay, regular pay, and gross pay

overtime = hrs_worked - 40
overtime_pay = pay_rate * 1.5 * overtime
reghour_pay = 40 * pay_rate
gross_pay = reghour_pay + overtime_pay

# Compute employee information 


print("Hours Worked       Pay Rate    OverTime    OverTime Pay    RegHour Pay   Gross Pay")
print(f"-------------------------------------------------------------------------------------------")

print(f'{hrs_worked:<20.1f}{pay_rate:<11.1f}{overtime:<12.2f}{overtime_pay:<16.2f}${reghour_pay:<14.2f}${gross_pay:<8.2f}')








