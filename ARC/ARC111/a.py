n, m = map(int, input().split())
r = pow(10, n, m)
q = pow(10, n, m**2)
r %= m**2
ans = (q-r)
ans //= m
print(ans)
