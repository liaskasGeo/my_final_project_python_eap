my_list = [5,4,3,2,5,6,7,8,9,1]
my_list.sort()

maximum = my_list[0]
i = 1

while i < len(my_list):
    if my_list[i] > maximum:
        maximum = my_list[i]
    i += 1

print("To megisto einai:", maximum)






