my_list =[1,3,5]
print(my_list[-1]) # 5
print(my_list[-2]) # 3
print(my_list[-3]) # 1
print(my_list) # [1, 3, 5]

print("=============")

my_list[-2] = 6
print(my_list)              # changed to [1, 6, 5]
my_list[-3] = 4
print(my_list)              # changed to [4, 6, 5]

print("=================")

my_list = ["a","b","c","d","e",]
print(my_list)

my_new_list = my_list[1:4] #['b', 'c', 'd']
print(my_new_list)
my_new_list_2 = my_list[2:3] # ['c'] (apo to 2 mexri to 2) (0 ->1 -> 2)
print(my_new_list_2)
my_newest_list = my_list[:] # oli i lista (ANTIGRAFI LISTAS)
print(my_newest_list)
print(my_newest_list[-4:-2]) # ara to 2 kai to 3

print(my_newest_list[:4]) # mexri to pro-teleuteo
print(my_newest_list[:-1]) # mexri to pro-teleuteo
print(my_newest_list[-5:])#oli i lista
print(my_newest_list[-5:5])#oli i lista
print(my_newest_list[0:]) # oli i lista, apo tin arxi mexri to telos
