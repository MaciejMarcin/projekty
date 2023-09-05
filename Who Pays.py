import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


number_of_names = len(names) - 1

random_person = random.randint(0,number_of_names)

final = names[random_person]

print(f"{final} is going to buy the meal today!")

input()
