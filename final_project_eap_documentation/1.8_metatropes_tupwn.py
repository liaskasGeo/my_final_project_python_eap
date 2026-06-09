#Δεκαδικός
from pyexpat.errors import messages

a_float = 3.84
print(a_float)
print("Ο τύπος είναι: ",type(a_float),"\n")

#Μετατροπή σε ακέραιο
to_int = int(a_float)
print(to_int)
print("Ο τύπος είναι: ",type(to_int),"\n")

#Μετατροπή σε string
to_str=str(a_float)
print(to_str)
print("Ο τύπος είναι: ",type(to_str),"\n","\n")


age = 19
name = "John Doe"
message = name + " is " + str(age) + " years old." #Μετατρέπει σε string το age
print(message)