parastasi  = 10 + 50 > 10 + 40 # Πρώτα οι πράξεις και μετά ο σχεσιακός τελεστής
print(parastasi)

parastasi2  = 10 + 50 > 10 + 40 or 10 + 30 > 10 + 50
print(parastasi2)

#The Geek Factor
print("---------Geek Factor----------")
is_geek = True

computer_hours = 12

sport_hours = 1

print("Κάθομαι στον υπολογιστή περισσότερες απο 5 ώρες , αθλούμαι λιγότερες απο 2 ώρες και πιστεύω οτι είμαι geek")
geek_factor = computer_hours > 5 and sport_hours < 2 and not is_geek
print(geek_factor)


