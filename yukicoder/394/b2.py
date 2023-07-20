N = int(input())
S = set()
for x in range(N+1):
    if x**2 > N:
        break
    for y in range(N+1):
        if y**2 > N:
            break
        if x == 0 and y == 0:
            continue
        if (N-x*y) % (x+y) == 0:
            z = (N-x*y)//(x+y)
            if z >= 0:
                S.add((x, y, z))
                S.add((x, z, y))
                S.add((y, x, z))
                S.add((y, z, x))
                S.add((z, y, x))
                S.add((z, x, y))


print(len(S))
for c in S:
    print(*c)
