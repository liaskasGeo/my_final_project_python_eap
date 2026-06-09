for a in range(1,20+1):
    for b in range(1,20+1):
        for c in range(1,20+1):
            if a*a + b*b == c * c:
                print(f"a = {a} * {a} = {a*a} \nb = {b} * {b} = {b*b}\nc = {c} * {c} = {c*c}")
                print(f"a = {a*a} + b = {b*b} = {a*a + b*b}")
                print(f"{(a*a)} + {b*b} = {c*c} ")
                print(f"({a},{b},{c})")

    print("")
