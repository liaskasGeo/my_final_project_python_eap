#metatropi list se tuple
my_list = [1,2,3]
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple)

#metatropi tuple se list
my_tuple2 = (1,2,3)
my_list2 = list(my_tuple)

#metatropi range se list
my_list3 = list(range(4)) # [0,1,2,3]
print(my_list3)

#metatropi string se lista
msg = "Hello"
print(list(msg))
