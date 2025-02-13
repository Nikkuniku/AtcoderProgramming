M, K = map(int, input().split())
s = set()
for i in range(1 << M):
    j = i ^ K
    if (1 << M) < j:
        exit(print(-1))
    if j < i:
        i, j = j, i
    s.add((i, j))
ans = []
if K == 0:
    for i in range(1 << M):
        ans.append(i)
        ans.append(i)
else:
    pairs = list(s)
    if len(pairs) % 2 != 0:
        exit(print(-1))
    for i in range(len(pairs)):
        if i % 2 != 0:
            continue
        a, b = pairs[i]
        c, d = pairs[i + 1]
        ans.append(a)
        ans.append(b)
        ans.append(c)
        ans.append(d)
        ans.append(b)
        ans.append(a)
        ans.append(d)
        ans.append(c)
print(*ans)
