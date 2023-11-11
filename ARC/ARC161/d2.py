N, D = map(int, input().split())
if N * D > N * (N - 1) // 2:
    exit(print("No"))
if D == 1:
    res = []
    for i in range(N - 1):
        res.append((i + 1, i + 2))
    if N > 2:
        res.append((N, 1))
    print("Yes")
    for c in res:
        print(*c)
    exit()
for k in range(N):
    if k - 1 >= 2 * D:
        break
ans = []
for i in range(N):
    for j in range(i + 1, min(N, i + k), 1):
        ans.append((i + 1, j + 1))
        if len(ans) == N * D:
            break
    if len(ans) == N * D:
        break
print("Yes")
for c in ans:
    print(*c)
