H, W = map(int, input().split())
C = [input() for _ in range(H)]
ans = [0]*W
for j in range(W):
    for i in range(H):
        if C[i][j] == '#':
            ans[j] += 1
print(*ans)
