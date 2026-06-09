day = "Sunday"
tired = True

if day == "Saturday":                #if this condition is true then it doesnt move to elif .This has to be False in order to move
    print("I will read a bit.")
elif day == "Sunday":
    if tired:
        print("I wont study at all")
    else:
        print("I will stydy a lot")
else:
    print("I will study")

#another way to set an if - else (not recommended)

print("LALALA") if day == "Wednesday" or "wednesday" else print("Today is",day)

condition = int()
if condition:
    pass # an theleis na valeis kati stin sunexeia den kanei kati
else:
    print()

number = int(input("Insert Number:"))

result = "odd" if number % 2 == 1 else "even" # den protinetai ,apla gia gnwsi

print(result)