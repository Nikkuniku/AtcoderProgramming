from random import randint

N = 20
M = randint(2, 10**9)
A = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i].append(randint(1, 9))
print(N, M)
for c in A:
    print(*c)
