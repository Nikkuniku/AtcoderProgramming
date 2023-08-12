H, W = map(int, input().split())
C = [list(input()) for _ in range(H)]
ans = [[0]*W for _ in range(2*H)]
for i in range(2*H):
    for j in range(W):
        ans[i][j] = C[i//2][j]
for c in ans:
    print(*c, sep="")
