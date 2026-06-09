numbers = [1,8,7,4,11,12,2,9,2,5]
search = 2

for number in numbers:
    if search ==number:
        print("Found it!")
        break
else: # when has break usually
    print("Didnt find it")

print("=======================")
if 2 in numbers:
    print("Found it!")

print("=======================")

for number in range(0,10):
    if number % 2 == 1:
        continue
    print(number)

