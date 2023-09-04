bill = input("What is the amount of the bill? \n")
number_of_people = input("How many people to split the bill? \n")
percent = input("What percentage of the tip you want to leave? \n")

tip = (int(percent) / 100) * float(bill)

bill_and_tip = float(bill) + tip

final_price = bill_and_tip / int(number_of_people)

x = round(final_price, 2)


print(f"Your bill is {x}$")

input()
