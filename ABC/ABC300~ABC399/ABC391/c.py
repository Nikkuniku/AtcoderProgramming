N, Q = map(int, input().split())
ans = []
res = 0
C = [1] * N
Pigeon = [i for i in range(N)]
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p, h = query[1:]
        p -= 1
        h -= 1
        i = Pigeon[p]
        if C[i] == 2:
            res -= 1
        C[i] -= 1
        if C[h] == 1:
            res += 1
        C[h] += 1
        Pigeon[p] = h
    elif query[0] == 2:
        ans.append(res)
print(*ans, sep="\n")
