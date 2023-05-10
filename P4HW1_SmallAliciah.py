
   # CTI-110

   # P4HW1 - Loop

   # Aliciah Small

   # 4/29/23

   

# Determine how many scores
grade_num = int(input('How many scores do you want to enter? '))

print()

# Create list

score_list = []

# Create loop

for num in range(1,grade_num+1):

  print("Enter score #",num,": ", end = " ")
  score = float(input())

  # Score must be positive

  if score < 0 or score > 100:
    print('INVALID Score entered!!!!')
    print('Score should be between 0 and 100')
    print('Enter score #',num,": ", 'again: ',end =' ')
    score = float(input())
    break

score_list.append(score)

low = min(score_list)
high = max(score_list)
sum1 = sum(score_list)
avg = sum(score_list)/6

# determine lowest score of list

print(f"\n------------Results------------")
print(f'{"Lowest Score   : ":<21}{low:<21}')

# drop lowest score from list
score_list.pop()

# create new list
print(f'{"Modified List  : ":<21}{high:<21}')

# determine average score and final grade average
print(f'{"Scores Average : ":<21}{sum1:<21}')
print(f'{"Grade          : ":<21}{avg:.2f}')

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


