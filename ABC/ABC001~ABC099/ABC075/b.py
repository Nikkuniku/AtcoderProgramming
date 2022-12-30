h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))

ans = [[0]*w for _ in range(h)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(h):
    for j in range(w):
        cnt = 0
        for k in range(8):
            nx = i+dx[k]
            ny = j+dy[k]
            if 0 <= nx < h and 0 <= ny < w:
                if s[nx][ny] == '#':
                    cnt += 1
        ans[i][j] = cnt

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = s[i][j]

for i in range(h):
    print(''.join(map(str, ans[i])))
