# Determining days in feb during leap year
def days_in_feb(user_year):
    if user_year % 100 == 0:
        if user_year % 400 == 0:
            return 29
        else:
            return 28
    else:
        if user_year % 4 == 0:
            return 29
        else:
            return 28
    
if __name__ == '__main__':
    # insert a year 
    user_year = int(input())
    # determine number of days
    days = days_in_feb(user_year)
    
    # print statement 
    print(f'{user_year} has {days} days in February.')
    