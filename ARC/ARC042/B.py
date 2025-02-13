from more_itertools import pairwise

x, y = map(int, input().split())
N = int(input())
Points = [list(map(int, input().split())) for _ in range(N)]
Points.append(Points[0])
ans = 1 << 60
for p1, p2 in pairwise(Points):
    xi, yi = p1
    xj, yj = p2
    a = yi - yj
    b = xj - xi
    c = xi * yj - xj * yi
    d = abs(a * x + b * y + c) / (a**2 + b**2) ** 0.5
    ans = min(ans, d)
print(ans)
