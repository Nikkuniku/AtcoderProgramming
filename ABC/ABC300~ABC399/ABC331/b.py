N, S, M, L = map(int, input().split())
ans = 1 << 60
for i in range(101):
    for j in range(101):
        for k in range(101):
            if (6 * i) + (8 * j) + (12 * k) >= N:
                tmp = S * i + M * j + L * k
                ans = min(ans, tmp)
print(ans)
