N = int(input())
S = [input() for _ in range(N)]
T = sorted([(S[i], i) for i in range(N)])
ans = [0] * N
for i in range(N - 1):
    p = T[i][0]
    q = T[i + 1][0]
    a, b = T[i][1], T[i + 1][1]
    M = min(len(p), len(q))
    isNotEqual = False
    for j in range(M):
        if p[j] != q[j]:
            ans[a] = max(ans[a], j)
            ans[b] = max(ans[b], j)
            isNotEqual = True
            break
    if not isNotEqual:
        ans[a] = max(ans[a], M)
        ans[b] = max(ans[a], M)
print(*ans, sep="\n")
