N = int(input())
S = input()
Q = int(input())
INF = 1 << 60
k = INF
Query = []
for i in range(Q):
    t, x, c = input().split()
    t = int(t)
    x = int(x)
    Query.append((t, x, c))
    if t == 2 or t == 3:
        k = i
ans = list(S)
for i in range(Q):
    t, x, c = Query[i]
    if i < k:
        if t == 1:
            ans[x - 1] = c
        else:
            continue
    elif i == k:
        if t == 2:
            for j in range(N):
                ans[j] = ans[j].lower()
        elif t == 3:
            for j in range(N):
                ans[j] = ans[j].upper()
    elif i > k:
        if t == 1:
            ans[x - 1] = c
print(*ans, sep="")
