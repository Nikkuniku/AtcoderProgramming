n, m = map(int, input().split())
p = pow(10, n, m**2)
ans = (p//m) % m
print(ans)
