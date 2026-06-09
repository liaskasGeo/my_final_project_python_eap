hours = int(input("Δώσε ώρες: "))
minutes = int(input("Δώσε λεπτά: "))
seconds = int(input("Δώσε δευτερόλεπτα: "))

if hours < 10:
    message1 = "0" + str(hours)
else:
    message1 = str(hours)

if minutes < 10:
    message2 = "0" + str(minutes)
else:
    message2 = str(minutes)

if seconds < 10:
    message3 = "0" + str(seconds)
else:
    message3 = str(seconds)

print(message1,":",message2,":",message3)

