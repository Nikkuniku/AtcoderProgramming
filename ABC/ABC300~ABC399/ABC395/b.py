N = int(input())
ans = [["."] * N for _ in range(N)]
for i in range(N):
    j = N + 1 - (i + 1)
    if i >= j:
        continue
    j -= 1
    for a in range(i, j + 1):
        for b in range(i, j + 1):
            if i % 2 == 0:
                ans[a][b] = "#"
            else:
                ans[a][b] = "."
for c in ans:
    print(*c, sep="")
