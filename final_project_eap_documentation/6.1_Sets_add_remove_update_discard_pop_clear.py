my_set = {1,2,3}
print("1.My set is: ",my_set)
my_set.add(5)
print("2.my_set.add(5) : Now set is: ",my_set)
my_set.add(3)
print("3.my_set.add(3) Now set is :",my_set,"(Because its dublicate)")
my_set.update((1,4,5))
print("We added a tuple my_set.update((1,4,5)),the only not duplicate is 4 so now set is :",my_set)

#set_name.remove(element) (can cause Error if element not found)
#set_name.discard(element) (removes element , doesnt cause error)
#set_name.pop() (removes an element from set)
#set_name.clear() (removes all elements from set)

#set_name = set(collection) makes collection into a set
print("=======================")
my_list = [number for number in range(10) if number % 2 == 0]
print("my_list is : ",my_list)
my_set = set(my_list)
print("my_set is my_list:",my_set)
my_set.discard(2)
print("my_set after discard(2) is:",my_set)
# my_set.remove(2) #error because there's no 2 to remove and we said that remove causes errors if not found
