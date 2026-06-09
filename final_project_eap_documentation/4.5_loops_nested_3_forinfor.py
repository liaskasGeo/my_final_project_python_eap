N=5

for i in range(0, N):
    for j in range(0,N-i-1):
        print("",end=" ") # Tha tupwnei N-i-1 Spaces dld 5 - 0 - 1 = 4 ,meta 5 - 1 - 1 = 3 , meta 5 - 2 - 1 = 2 ,meta 5 - 3 - 1 = 1
    for j in range(0, 2*i+1):
        print("*",end="") # tin prwti fora tiponei (4 kena logw tou panw j kai ena *),tin deuteri (3 kena , 2 asterakia) , (2 kena , 3 asterakia) ktlp
    print("")


