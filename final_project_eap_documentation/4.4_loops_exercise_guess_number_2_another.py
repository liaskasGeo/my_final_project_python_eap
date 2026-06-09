#Guess number psounis solution

hidden = 43
count = 0
max_guess = 3
guess =int(input("Give a number: "))
active = True

while True:
        count+=1
        if count == max_guess:
            print("You lost.")
            break

        if guess > hidden:
            print("Lower number.")
        elif guess < hidden:
            print("Higher number.")
        else:
            print("You have found it.")
            break

        guess = int(input("Give a number: "))