K, G, M = map(int, input().split())
g = 0
m = 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        while m > 0 and g < G:
            m -= 1
            g += 1
print(g, m)
