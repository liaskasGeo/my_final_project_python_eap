player_1_zaria_1 = int(input("1h zaria prwtou paixti: "))
player_1_zaria_2 = int(input("2h zaria prwtou paixti: "))

player_2_zaria_1 = int(input("1h zaria deuterou paixti:"))
player_2_zaria_2 = int(input("2h zaria deuterou paixti:"))

player_1_total = player_1_zaria_1 + player_1_zaria_2
player_2_total = player_2_zaria_1 + player_2_zaria_2

if player_1_total > player_2_total:
    print("Tha peksei o prwtos paixtis prwtos.")

elif player_2_total > player_1_total:
    print("Tha peksei o deuteros paixtis prwtos.")

else:
    print("Isopalia")

