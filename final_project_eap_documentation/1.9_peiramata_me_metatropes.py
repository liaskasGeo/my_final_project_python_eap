an_int = 5
a_float = 10.0
print(an_int + a_float)
a_bool = True

a_string = "message"
#print(an_int + a_string) ERROR
print(str(an_int) + a_string)
print()
print("Result: ",an_int + a_bool) # 5 + 1(True = 1 , so 5 + 1 = 6 )
a_bool = False
print("Result: ",an_int + a_bool)# This Case a_bool is False = 0 so print is 5 + 0 = 5
