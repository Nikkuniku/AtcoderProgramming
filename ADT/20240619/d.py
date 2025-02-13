K, G, M = map(int, input().split())
g, m = 0, 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        while g < G and m > 0:
            g += 1
            m -= 1
print(g, m)
