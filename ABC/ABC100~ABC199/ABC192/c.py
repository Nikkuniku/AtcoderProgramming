N, K = map(int, input().split())
a0 = N
for _ in range(K):
    g1 = int(''.join(sorted(list(str(a0)), reverse=True)))
    g2 = int(''.join(sorted(list(str(a0)))))
    f = g1-g2
    a0 = f
print(a0)
