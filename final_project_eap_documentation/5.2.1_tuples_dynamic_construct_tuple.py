my_list = []

for i in range(1, 11):
    number = int(input(f"Enter {i} number(10-20): "))

    while number < 10 or number > 20:
        number = int(input("Between 10 and 20 please: "))

    my_list.append(number)

print(my_list)
my_new_list = my_list[:]
print(my_new_list)
for item in range(len(my_new_list)):
    my_new_list[item] = my_new_list[item] ** 2

my_new_list = sorted(my_new_list)
print("My new sorted list is :",my_new_list)

my_tuple = tuple(my_new_list)
print("My sorted tuple is: ",my_tuple)












