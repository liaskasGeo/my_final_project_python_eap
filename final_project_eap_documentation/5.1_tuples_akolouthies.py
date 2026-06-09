#sequence.ops
numbers = (1,2,3,4,3,2,3,3)
print("Length:"+ str(len(numbers)))
print("min:"+ str(min(numbers)))
print("max:"+ str(max(numbers)))
print("How many numbers 3 :"+ str(numbers.count(3))) #poses fores uparxei to 3 mesa sto tuple
print("pos of a 3: "+ str(numbers.index(3,4))) # vres mou ena 3 , ksekinontas apo tin thesi 4

#brain.damage.py
print("-------------------------------------------")

my_list = [1,2,3]
new_list = ((my_list * 2)[1:5] + list((7,8)))*4
print(f"{my_list} + {new_list} = {my_list + new_list}")
print(" The numbers of 2 in my_list+new_list are :",str((my_list+new_list).count(2)))

print("====================================")
#copy list
list1 = [1,2,3]
list2 = list1
list2[0] = 4
print(list1) #[4, 2, 3] ?????????? wrong
print(list2) #[4, 2, 3] correct

#copy sequence
old_list_1 = [1,2]
new_list_2 = old_list_1[:] #copy 1 method (we usually choose this method cause its faster)
new_list_2[0] = 4 #assign to first value number 4 
print("New list is a copy of old list: ",new_list)
#method copy
# new_list = old_list_1.copy() # copy 2 method (slower)
print("Old list: ",old_list_1)
print("New list: ",new_list_2)