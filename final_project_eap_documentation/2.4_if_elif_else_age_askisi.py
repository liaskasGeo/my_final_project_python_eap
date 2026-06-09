age = int(input("Eisagete ilikia: "))

if age < 18:
    print("Anilikos")
elif 18 <= age <= 65:       # elif age >= 18 and age <= 65:
    print("Enilikos")
else:
    print("Sintaksiouxos")