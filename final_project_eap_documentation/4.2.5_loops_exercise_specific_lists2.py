N = int(input("Step one, give number: "))
while N<3 or N>20:
    N = int(input("Give number between 3-20: "))

numbers = []
for count in range(1,N+1):
    numbers.append(input("Give " + str(count) + "th number: "))

numbers.sort()
print(numbers)