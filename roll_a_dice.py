import random

print("Welcome!")

decision = input("Do you want to roll a dice. (Y/N): ")

while (decision == "y"):
    
    number = random.randint(1, 6)

    if(number == 1):
        print("\n[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]\n")

    elif(number == 2):
        print("\n[-----]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[-----]\ny")

    elif(number == 3):
        print("\n[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]\n")

    elif(number == 4):
        print("\n[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]\n")

    elif(number == 5):
        print("\n[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]\n")

    elif(number == 6):
        print("\n[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]\n")

    decision = input("Do you want to play again? (Y/N): ")
    print("Thank you for playing!") if (decision != "y") else None 

print("Bye!")
