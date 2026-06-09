my_city_list = ["Athens","Berlin","London","Jakarta","Italy"]

for city in range(0,len(my_city_list)):
    if city % 2 == 0:
        print(my_city_list[city])

print("\n")

my_list = ["Athens","Berlin","London","Jakarta","Italy"]

for i in range(0, len(my_list), 2):
    print(my_list[i])
