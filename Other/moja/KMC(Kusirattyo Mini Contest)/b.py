H, W = map(int, input().split())
S = [['.']*(W+2)]
for _ in range(H):
    S.append(['.']+list(input())+['.'])
S.append(['.']*(W+2))
ans = 0
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for i in range(1, H+1):
    for j in range(1, W+1):
        if S[i][j] == '#':
            for dx, dy in dxy:
                ni = i+dx
                nj = j+dy
                if S[ni][nj] == '.':
                    ans += 1
print(ans)
