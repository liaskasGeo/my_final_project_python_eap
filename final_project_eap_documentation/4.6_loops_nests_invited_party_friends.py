best_friends = ["Geo","Maria","Thanos","Elena"]
invited_friends = []

guests = ["Giannis","Christos","Nausika","Nikos","Geo","Jane","John","Jim","Tom","Brad","Thanos"]

print("If at least 2 of your friends are invited consider go to the party.")
for friend in best_friends:
    if friend in guests:
        print(friend,"is invited!")
        invited_friends.append(friend)
print(invited_friends)
print("The number of your friends that are invited are: ",len(invited_friends))
if len(invited_friends) < 2:
    print("I wont come")
else:
    print("I am coming too!")
for friend in best_friends:
    if friend not in guests:
        print("Sorry",friend,"you are not invited")













