H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
a, b, c, d = 1 << 60, -1, 1 << 60, -1
for i in range(H):
    for j in range(W):
        if S[i][j] == "#":
            a = min(a, i)
            b = max(b, i)
            c = min(c, j)
            d = max(d, j)
ans = "Yes"
for i in range(a, b + 1):
    for j in range(c, d + 1):
        if S[i][j] == ".":
            ans = "No"
            break
print(ans)
