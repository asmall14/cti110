# CTI-110

# P4HW2 - Salary Calculator

# Aliciah Small

# 4/29/2023

# This program determines employee pay.



#establish loop; couldn't figure out how to establish infinite loop according to input
for num in range(50):

    # Terminate loop if input is 'done' or 'Done'

    emp_name = input('Enter employee\'s name or "Done" to terminate: ')
    if emp_name == 'done' or emp_name == "Done":

        emp_names = [num]
        
        sum_emp_name = sum(emp_names)
        
        print(f' Total number of employees entered: ',sum_emp_name)
        print(f' Total amount paid for overtime: ')
        print(f' Total amount paid for regular hours: ')
        print(f' Total amount paid in gross: ')

        break

    # Calculate employee hours and pay rate
    
    print('How many hours did', emp_name, 'work? ',end =" ")
    hrs_worked = float(input())

    print('What is', emp_name,'\'s pay rate? ',end =" ")
    pay_rate = float(input())

    print()

    # Overtime hours cannot be negative

    overtime = hrs_worked - 40
    if overtime <= 0:
            overtime = 0

    overtime_pay = pay_rate * 1.5 * overtime
    reghour_pay = hrs_worked * pay_rate
    gross_pay = reghour_pay + overtime_pay

    # Compute employee information in a chart

    print('Employee name: ', emp_name)

    print()
 

    print("Hours Worked       Pay Rate    OverTime    OverTime Pay    RegHour Pay   Gross Pay")
    print(f"-------------------------------------------------------------------------------------------")

    print(f'{hrs_worked:<20.1f}{pay_rate:<11.2f}{overtime:<12.1f}{overtime_pay:<16.2f}${reghour_pay:<14.2f}${gross_pay:<8.2f}')


    print()
    print()


# I didn't finish the code...
