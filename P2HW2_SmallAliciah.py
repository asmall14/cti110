
   # CTI-110

   # P2HW2 - List

   # Aliciah Small

   # 4/8/23

   #
   


mod_1 = float(input("Enter grade for Module 1: "))

mod_2 = float(input("Enter grade for Module 2: "))

mod_3 = float(input("Enter grade for Module 3: "))

mod_4 = float(input("Enter grade for Module 4: "))

mod_5 = float(input("Enter grade for Module 5: "))

mod_6 = float(input("Enter grade for Module 6: "))


mod_list = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

mod_list_min = min(mod_list)
mod_list_high = max(mod_list)
mod_list_sum = sum(mod_list)
mod_list_avg = sum(mod_list)/6


print(f"\n------------Results------------")

print(f'{"Lowest Grade: ":<21}{mod_list_min:<21}')
print(f'{"Highest Grade: ":<21}{mod_list_high:<21}')
print(f'{"Sum of Grades: ":<21}{mod_list_sum:<21}')
print(f'{"Average: ":<21}{mod_list_avg:.2f}')

print("-------------------------------")
