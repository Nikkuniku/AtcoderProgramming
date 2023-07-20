H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
ans = []
for i in range(H):
    for j in range(W):
        for k in range(8):
            tmp = []
            for t in range(5):
                x = i+t*dx[k]
                y = j+t*dy[k]
                if (not 0 <= x < H) or (not 0 <= y < W):
                    break
                tmp.append(S[x][y])
            if ''.join(tmp) == 'snuke':
                for t in range(5):
                    ans.append((i+t*dx[k]+1, j+t*dy[k]+1))
                for a in ans:
                    print(*a)
                exit()
