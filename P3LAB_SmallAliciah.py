is_leap_year = False
   
input_year = int(input())

#determining if year is divisible by 4
if input_year % 4 == 0:
#determining if year is a century year
    if input_year % 100 == 0:
#determining if year is divisible by 400
        if input_year % 400 == 0:
            is_leap_year = True 
            
    else: 
        is_leap_year = True
        
if is_leap_year: 
    print(input_year,'- leap year')
    
else:
    print(input_year,'- not a leap year')
