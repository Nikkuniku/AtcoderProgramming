from bisect import bisect_left
X = int(input())

tousasuu = set()
INF = 10**18
for i in range(1, 10):
    tousasuu.add(i)
    for j in range(-9, 10, 1):
        x = i
        y = (i+j) % 10
        p = str(i)
        while y-x == j:
            p += str(y)
            if int(p) <= INF:
                tousasuu.add(int(p))
                x, y = y, (y+j) % 10
            else:
                break

tousasuu = sorted(list(tousasuu))
ans_index = bisect_left(tousasuu, X)
print(tousasuu[ans_index])
