my_list = []
for number in range(3):
    my_list.append(number)
print(my_list)

#Comprehension / Perigrafikes
#      append(number)
my_list2 = [number for number in range(3)]
print(my_list2)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist2 = [fruit for fruit in fruits]
print(newlist2)

#perigrafi my_list = [number for number in range(10) if number%2 ==0]

# [            → ξεκινάμε να φτιάξουμε μία λίστα
# number       → το στοιχείο που θα μπει μέσα στη λίστα
# for          → για κάθε
# number       → μεταβλητή που παίρνει τιμές
# in           → από
# range(10)    → τους αριθμούς 0 έως 9
# if           → μόνο αν
# number       → ο αριθμός
# %            → το υπόλοιπο της διαίρεσης
# 2            → με το 2
# == 0         → είναι ίσο με 0 (δηλαδή ο αριθμός είναι ζυγός)
# ]            → τέλος της λίστας

