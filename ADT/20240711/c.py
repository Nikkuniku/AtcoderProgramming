N = int(input())
T = input()
x, y = 0, 0
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
d = 0
for t in T:
    if t == "S":
        dx, dy = dxy[d]
        x += dx
        y += dy
    else:
        d += 1
        d %= 4
print(x, y)
