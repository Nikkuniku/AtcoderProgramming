X = int(input())
N = 1
Y = 1
while 1:
    N += 1
    Y *= N
    if X == Y:
        exit(print(N))
