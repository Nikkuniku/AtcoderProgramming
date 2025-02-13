H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
pone = []
for i in range(H):
    for j in range(W):
        if S[i][j] == "o":
            pone.append((i, j))
ans = 0
for k in range(2):
    ans += abs(pone[0][k] - pone[1][k])
print(ans)
