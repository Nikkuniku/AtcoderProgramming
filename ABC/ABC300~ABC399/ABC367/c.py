from itertools import product

N, K = map(int, input().split())
R = list(map(int, input().split()))
P = list(product(range(1, 6), repeat=N))
ans = []
for c in P:
    isOK = True
    tmp = 0
    for i in range(N):
        if c[i] > R[i]:
            isOK = False
            break
        tmp += c[i]
    if isOK and tmp % K == 0:
        ans.append(c)
ans.sort()
for c in ans:
    print(*c)
