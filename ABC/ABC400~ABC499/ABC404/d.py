from itertools import product

N, M = map(int, input().split())
P = list(product([0, 1, 2], repeat=N))
C = list(map(int, input().split()))
Zoos = [[] for _ in range(N)]
for i in range(M):
    K, *A = list(map(int, input().split()))
    for a in A:
        Zoos[a - 1].append(i)
ans = 1 << 60
for bits in P:
    temp = 0
    seen = [0] * M
    for i in range(N):
        cnt = bits[i]
        for a in Zoos[i]:
            seen[a - 1] += cnt
        temp += C[i] * cnt
    isOK = True
    for j in range(M):
        if seen[j] < 2:
            isOK = False
            break
    if isOK:
        ans = min(ans, temp)
print(ans)
