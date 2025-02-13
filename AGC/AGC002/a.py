a, b = map(int, input().split())
if a < 0:
    if b >= 0:
        print("Zero")
    else:
        tmp = abs(a) - abs(b) + 1
        if tmp % 2 == 0:
            print("Positive")
        else:
            print("Negative")
elif a == 0:
    print("Zero")
else:
    print("Positive")
