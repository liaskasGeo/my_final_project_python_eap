active = True

while active:
    user_input = input("Type string or 'quit': ")

    if user_input == "quit":
        print("Bye Bye")
        active = False
    else:
        print(f"Why {user_input} ?!")