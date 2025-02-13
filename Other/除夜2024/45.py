N = int(input())
ans = []
for x in range(N + 1):
    for y in range(N + 1):
        for z in range(N + 1):
            if x + y + z <= N:
                ans.append((x, y, z))
for c in ans:
    print(*c)
