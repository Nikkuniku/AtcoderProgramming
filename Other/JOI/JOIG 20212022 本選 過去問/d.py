from collections import defaultdict
H, W = map(int, input().split())
N = int(input())
d = {}
for _ in range(N):
    a, b = map(int, input().split())
    if (a, b) not in d:
        d[(a, b)] = 1
    else:
        d[(a, b)] += 1

dxy = [(1, 0), (1, -1), (1, 1), (0, -1), (0, 0),
       (0, 1), (-1, -1), (-1, 0), (-1, 1)]
ans = 0
Keys = list(d.keys())
for a, b in Keys:
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            tmp = 0
            for dx, dy in dxy:
                if (a+i+dx, b+j+dy) in d:
                    tmp += d[(a+i+dx, b+j+dy)]
            ans = max(ans, tmp)
print(ans)
