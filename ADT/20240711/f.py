from collections import defaultdict

N, M, H, K = map(int, input().split())
S = input()
d = defaultdict(int)
for _ in range(M):
    x, y = map(int, input().split())
    d[x, y] += 1
x, y = 0, 0
ans = "Yes"
for s in S:
    H -= 1
    if s == "R":
        x += 1
    elif s == "L":
        x -= 1
    elif s == "U":
        y += 1
    elif s == "D":
        y -= 1
    if H < 0:
        ans = "No"
        break
    if H < K and d[x, y] > 0:
        H = K
        d[x, y] -= 1
print(ans)
