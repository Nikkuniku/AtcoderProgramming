N = int(input())
d = dict()
A, B = map(int, input().split())
M = -1
for _ in range(N):
    p, q, r, s = map(int, input().split())
    for i in range(p, r+1):
        for j in range(q, s+1):
            if (i, j) in d:
                d[(i, j)] += 1
            else:
                d[(i, j)] = 1
            M = max(M, d[(i, j)])
ans = list(d.values()).count(M)
print(M)
print(ans)
