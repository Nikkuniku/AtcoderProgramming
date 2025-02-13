X = int(input())
L = 1000
for a in range(-L, L + 1):
    for b in range(-L, L + 1):
        if a**5 - b**5 == X:
            exit(print(a, b))
