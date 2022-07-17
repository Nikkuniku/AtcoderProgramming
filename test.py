from math import ceil
ans = []
for a in range(1, 1000):
    for b in range(1, 1000):
        p = ceil(b/a)
        q = -(-b//a)

        if p != q:
            ans.append((a, b, p, q))

print(*ans, sep="\n")
