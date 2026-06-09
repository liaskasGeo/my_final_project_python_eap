i = 1
my_list_sum = 0
my_list = []

while i <= 10:
    print(f"Eisagete {i} arithmo: ")
    input_1 = int(input())

    my_list.append(input_1)
    my_list_sum += input_1

    print("Lista:", my_list)
    print("Athroisma mexri twra:", my_list_sum)

    i += 1
