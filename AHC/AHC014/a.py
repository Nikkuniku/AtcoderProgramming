import random
n, m = map(int, input().split())
points = []
used = set()
X_p = [[] for _ in range(n)]
Y_p = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    points.append((x, y))
    used.add((x, y))
    X_p[x].append(y)
    Y_p[y].append(x)
grid = [[[] for _ in range(n)] for _ in range(n)]


for _ in range(20):
    while True:
        a = random.randint(0, len(used))
        b = random.randint(0, len(used))
        c = random.randint(0, len(used))
        if len(set([a, b, c]) == 3:
            break

    x1, y1=points[a]
    x2, y2=points[b]
    x3, y3=points[c]
    x4=x1 ^ x2 ^ x3
