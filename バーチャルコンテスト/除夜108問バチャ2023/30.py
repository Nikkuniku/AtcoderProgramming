N = int(input())
point = [list(map(int, input().split())) for _ in range(N)]


def dist(sx, sy, gx, gy):
    return ((sx-gx)**2 + (sy-gy)**2)**0.5


ans = 0
for i in range(N):
    for j in range(i+1, N):
        ans = max(ans, dist(*point[i], *point[j]))
print(ans)
