N, M = map(int, input().split())
ans = []
if N % 2 != 0:
    for j in range(M):
        ans.append((1 + j, N - j))
else:
    for j in range(M):
        if 1 + j <= N // 4:
            ans.append((1 + j, N - j))
        else:
            ans.append((1 + j, N - 1 - j))
for c in ans:
    print(*c)
