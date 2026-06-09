#Even numbers create list
my_list = []
for number in range(10):
    if number % 2 == 0:
        my_list.append(number)
print(my_list)

#Even numbers create list / Comprehension / Perigrafikes
my_list = [number for number in range(10) if number%2 ==0]
print(my_list)

#For in me if else
my_list = []
for number in range(10):
    if number%2 == 0:
        my_list.append(number)
    else:
        my_list.append(number/2)
print(my_list)

#For in me if else Comprehension / Perigrafikes

my_list = [number if number % 2 == 0 else number/2 for number in range(10)]
print(my_list)