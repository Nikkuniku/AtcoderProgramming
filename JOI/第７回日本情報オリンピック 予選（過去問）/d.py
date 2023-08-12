M = int(input())
Stars = [tuple(list(map(int, input().split()))) for _ in range(M)]
N = int(input())
Points = [tuple(list(map(int, input().split()))) for _ in range(N)]
S = set(Points)
for i in range(N):
    a, b = Points[i]
    x, y = Stars[0]
    dx = x-a
    dy = y-b
    isOK = True
    for j in range(1, M):
        c, d = Stars[j]
        sx, sy = c-dx, d-dy
        if (sx, sy) not in S:
            isOK = False
    if isOK:
        print(-dx, -dy)
        exit()
