Q = int(input())
ans = []
q = []
for _ in range(Q):
    t, p = input().split()
    p = int(p)
    if t == "1":
        q.append(p)
    elif t == "2":
        M = len(q)
        ans.append(q[M - p])
print(*ans, sep="\n")
