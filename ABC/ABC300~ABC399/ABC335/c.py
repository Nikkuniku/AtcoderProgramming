N, Q = map(int, input().split())
tatsu = []
for i in range(N):
    tatsu.append((i + 1, 0))
tatsu = tatsu[::-1]
ans = []
for i in range(Q):
    q, t = input().split()
    x, y = tatsu[-1]
    if q == "1":
        if t == "R":
            x += 1
        elif t == "L":
            x -= 1
        elif t == "U":
            y += 1
        elif t == "D":
            y -= 1
        tatsu.append((x, y))
    else:
        t = int(t)
        ans.append(tatsu[-t])

for c in ans:
    print(*c)
