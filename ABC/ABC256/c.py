h1, h2, h3, w1, w2, w3 = map(int, input().split())

arr = []
H1 = []
H2 = []
H3 = []
for a in range(1, 29):
    for b in range(1, 29):
        for c in range(1, 29):
            if a+b+c == h1:
                H1.append((a, b, c))
            if a+b+c == h2:
                H2.append((a, b, c))
            if a+b+c == h3:
                H3.append((a, b, c))

ans = 0
for a in H1:
    for b in H2:
        for c in H3:
            if a[0]+b[0]+c[0] == w1 and a[1]+b[1]+c[1] == w2 and a[2]+b[2]+c[2] == w3:
                ans += 1

print(ans)
