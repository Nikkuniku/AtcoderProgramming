H, W = map(int, input().split())
tokens = []
grid = [input() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'o':
            tokens.append((i, j))
ans = abs(tokens[0][0]-tokens[1][0])+abs(tokens[0][1]-tokens[1][1])
print(ans)
