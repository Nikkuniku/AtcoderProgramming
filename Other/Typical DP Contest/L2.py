from random import randint

N = int(input())
A = [[-1] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = A[j][i] = randint(-100, 100)
        if i == j:
            A[i][j] = 0
res = -(1 << 60)
for s in range(1 << (N - 1)):
    score = 0
    tmp = [0]
    for i in range(N - 1):
        if s & (1 << i):
            tmp.append(i + 1)
    tmp.append(N)
    for k in range(len(tmp) - 1):
        left = tmp[k]
        right = tmp[k + 1]
        for a in range(left, right):
            for b in range(left, right):
                score += A[a][b]
    res = max(res, score)
for c in A:
    print(*c)
print(res)
