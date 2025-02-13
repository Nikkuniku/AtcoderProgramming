N = int(input())
Point = [list(map(int, input().split())) + [i] for i in range(N)]
ans = []
for i in range(N):
    a, b, _ = Point[i]
    tmp = []
    maxdist = -1
    for x, y, j in Point:
        if i == j:
            continue
        dist = (x - a) ** 2 + (y - b) ** 2
        maxdist = max(maxdist, dist)
        tmp.append((dist, j + 1))
    tmp.sort(key=lambda x: x[1])
    for d, k in tmp:
        if d == maxdist:
            ans.append(k)
            break
print(*ans, sep="\n")
