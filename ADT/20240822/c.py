x, y = 0, 0
dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
dir = 0
N = int(input())
T = input()
for t in T:
    if t == "S":
        x += dxy[dir][0]
        y += dxy[dir][1]
    else:
        dir += 1
        dir %= 4
print(x, y)
