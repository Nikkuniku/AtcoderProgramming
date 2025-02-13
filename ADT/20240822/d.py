H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = [0] * W
for j in range(W):
    for i in range(H):
        ans[j] += C[i][j] == "#"
print(*ans)
