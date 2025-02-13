from random import randint

N = 50
A = [[] for _ in range(N)]
for i in range(N):
    for _ in range(N):
        A[i].append(randint(1, 20))
for c in A:
    print(*c)
