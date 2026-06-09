#Guess the number (my solution)
hidden_num = 67
tries = 5
active = True

while active:
    while tries >= 1:
        user_input = int(input("Guess the number: "))

        if user_input < 67:
            print("\n---- Higher number: ---- \n")
            tries -= 1
            print(f"You have,{tries},chances remaining")
        elif user_input > 67:
            print("\n---- Lower number: ---- \n")
            tries-=1
            print(f"You have,{tries},chances remaining")
        if tries == 0:
            print("You have failed")
            active = False
            break
        if user_input == 67:
            print("You found it!")
            active = False
            break





