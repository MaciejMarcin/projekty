print("""                
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ /
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___|
                """)

print("Welcome to Treasure Island. \n"
      "Your mission is to find the treasure")

path = input("Where do we go first, left or right? ")


if path.lower() == "left":
    path1 = input("Hey, you got it trough, do we want to swim or wait? ")
    if path1.lower() == "wait":
        path2 = input("Ufff, good choice \n" "There it is, three doors for you to choose - Red, Blue or Yellow? ")
        if path2.lower() == "yellow":
            print("YOU GOT IT! Treasure is yours!")
        elif path2.lower() == "red":
            print("Burned by fire. Game Over")
        elif path2.lower() == "blue":
            print("Eaten by beasts. Game Over")
        else:
            print("Game over")
    else :
        print("Attacked bt sharks. Game Over.")
else:
    print("Fall into a hole. Game Over")

input()
