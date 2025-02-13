from itertools import product

M, N = map(int, input().split())
X = list(map(int, input().split()))
P = product([i + 1 for i in range(M)], repeat=N)
ans = []
for p in P:
    isOK = True
    tmp = [[] for _ in range(M + 1)]
    for i, v in enumerate(p):
        tmp[v].append(i)
    for i in range(M + 1):
        if not tmp[i]:
            continue
        for j in range(len(tmp[i])):
            for k in range(j + 1, len(tmp[i])):
                A = p[tmp[i][j] : tmp[i][k]]
                if X[i - 1] not in A:
                    isOK = False
    if isOK:
        ans.append(p)
print(len(ans))
print(*ans, sep="\n")
