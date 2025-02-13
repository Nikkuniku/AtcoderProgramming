N = int(input())
ans = []
for x in range(N + 1):
    for y in range(N + 1):
        for z in range(N + 1):
            if x + y + z <= N:
                ans.append((x, y, z))
ans.sort(key=lambda x: x[2])
ans.sort(key=lambda x: x[1])
ans.sort(key=lambda x: x[0])
for c in ans:
    print(*c)
