# Είσοδος δεδομένων
hours = int(input("Δώσε ώρες: "))
minutes = int(input("Δώσε λεπτά: "))
seconds = int(input("Δώσε δευτερόλεπτα: "))

# Υπολογισμός
total_sec = hours * 3600 + minutes * 60 + seconds

# Έξοδος
print("Οι",hours,"ώρες,",minutes,"λεπτά,",seconds,"δευτερόλεπτα αντιστοιχούν σε: ",total_sec,"δευτερόλεπτα")


""" 
hours = 10 
minutes = 50
seconds = 15 

total_seconds = seconds
total_seconds+=minutes*60
total_seconds+=hours*3600
print(total_seconds)
"""