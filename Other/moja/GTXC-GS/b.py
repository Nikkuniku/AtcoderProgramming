N, K = map(int, input().split())
S = input()
from collections import defaultdict

d = defaultdict(lambda: -1)
for _ in range(N):
    a, x, y = map(int, input().split())
    d[x, y] = a
x, y = 0, 0
ball = 0
ans = []
for s in S:
    if s == "U":
        y += 1
    elif s == "D":
        y -= 1
    elif s == "R":
        x += 1
    elif s == "L":
        x -= 1
    ball += 1
    if d[x, y] != -1:
        if ball > d[x, y]:
            ans.append(ball - d[x, y])
            ball = d[x, y]
ans.append(ball)
print(len(ans))
print(*ans)
