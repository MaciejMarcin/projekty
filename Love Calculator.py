print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower()+name2.lower()
true = (names.count("t") + names.count("r") + names.count("u") + names.count("e"))
love = (names.count("l") + names.count("o") + names.count("v") + names.count("e"))

true_as_str = str(true)
love_as_str = str(love)
score = (true_as_str + love_as_str)
score_as_int = int(score)


if score_as_int < 10 or score_as_int > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score_as_int >= 40 and score_as_int <= 50:
    print(f"Your score is {score}, you are alright together ")
else:
    print(f"Your score is {score}")

input()









