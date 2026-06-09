my_list = []
n = int(input("1st step.Insert one number(3-20): "))
count=1

while n < 3 or n > 20:
    n = int(input("Insert numbers 3-20 please."))

while count <= n:
    n_2 = int(input("2nd step.Insert numbers(10-20): "))
    if n_2 < 10 or n_2 > 20:
        print("Insert numbers between 10-20 please.")
    else:
        print("Insert the next num please:")
        my_list.append(n_2)
        count+=1

my_list.sort()
print(my_list)


