n = int(input())
a = list(map(int, input().split()))
a = a[:8]
n = len(a)

mods = [[] for _ in range(200)]
for i in range(1, 1 << n):
    tmp = 0
    b = []
    for j in range(n):
        if (i >> j) & 1:
            tmp += a[j]
            b.append(j+1)

    tmp %= 200
    mods[tmp].append(b)

ans = 'No'
for p in mods:
    if len(p) > 1:
        a = p[0]
        b = p[1]
        print('YES')
        print(len(a), *a)
        print(len(b), *b)
        exit()
print(ans)
