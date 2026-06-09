N = 5

if N == 0 or N==1:
    print("Its not prime")
else:
    for i in range(2,N):
        if N % i == 0:
            print("Its not prime")
            break
    else:
        print("Its prime")
