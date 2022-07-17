h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(input())

points = []
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            points.append((i, j))

ans = abs(points[0][0]-points[1][0])+abs(points[0][1]-points[1][1])
print(ans)
