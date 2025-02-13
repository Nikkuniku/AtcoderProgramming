sab, sac, sbc = input().split()
if sab == "<":
    if sac == "<":
        if sbc == "<":
            print("B")
        else:
            print("C")
    else:
        print("A")
else:
    if sac == ">":
        if sbc == ">":
            print("B")
        else:
            print("C")
    else:
        print("A")
