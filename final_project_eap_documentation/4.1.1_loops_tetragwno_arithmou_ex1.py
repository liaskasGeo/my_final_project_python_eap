user_input = input("Give a number: ")
while user_input != "quit":
    print(int(user_input) ** 2)
    user_input = input("Give a number: ")


# active = True
#
# while active:
#     user_input = input("Eisagete enan arithmo (ή 'quit'): ")
#
#     if user_input == "quit":
#         print("Thank you")
#         active = False
#     else:
#         user_input = int(user_input)
#         user_input = user_input * user_input
#         print(user_input)