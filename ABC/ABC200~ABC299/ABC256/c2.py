h1, h2, h3, w1, w2, w3 = map(int, input().split())

ans = 0
for a11 in range(1, 29):
    for a12 in range(1, 29):
        x = h1-(a11+a12)
        if x <= 0:
            continue
        for a21 in range(1, 29):
            y = w1-(a11+a21)
            if y <= 0:
                continue
            for a22 in range(1, 29):
                z = h2-(a21+a22)
                v = w2-(a12+a22)
                if z <= 0:
                    continue
                if v <= 0:
                    continue

                p = h3-(y+v)
                q = w3-(x+z)
                if p == q and p > 0:
                    ans += 1

print(ans)
