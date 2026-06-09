x = int(input("Eisagete prwto arithmo: "))
y = int(input("Eisagete prwto arithmo: "))
z = int(input("Eisagete prwto arithmo: "))

#MAX
#Prwtos elegxos
if x > y:
    maximum = x
else:
    maximum = y

#Deuteros elegxos
if maximum < z:

    maximum = z

if (y == x and y == z) and (x == y and x == z):
    print("")
else:
    print("O megaliteros arithmos einai to : ",maximum)

#MIN
#Prwtos elegxos
if x < y:
    minimum = x
else:
    minimum = y

#Deuteros elegxos
if minimum > z:

    minimum = z

if (y == x and y == z) and (x == y and x == z):
    print("Oi arithmoi einai isoi")
else:
    print("O mikroteros arithmos einai to: ",minimum)
