# 🚨 Don't change the code below 👇
age = input("What is your current age?" )
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

months = 100 * 12
weeks = 100 * 52
days = 100 * 365


x = int(age)

monthsleft = months - x * 12
weeksleft = weeks - x * 52
daysleft = days - x * 365

print(f"You have {monthsleft} months, {weeksleft} weeks and {daysleft} days left. ")

input()
