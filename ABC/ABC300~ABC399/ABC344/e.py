N = int(input())
A = list(map(int, input().split()))
d = dict()
e = dict()
for i in range(N):
    if i < N - 1:
        d[A[i]] = A[i + 1]
    if 0 < i:
        e[A[i]] = A[i - 1]
d[-1] = A[0]
e[A[0]] = -1
d[A[-1]] = -2
e[-2] = A[-1]
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        y = query[2]
        p = d[x]
        d[x] = y
        d[y] = p
        e[y] = x
        e[p] = y
    elif query[0] == 2:
        x = query[1]
        p = d[x]
        q = e[x]
        d.pop(x)
        e.pop(x)
        d[q] = p
        e[p] = q
ans = []
now = d[-1]
while d[now] != -2:
    ans.append(now)
    now = d[now]
ans.append(now)
print(*ans)
