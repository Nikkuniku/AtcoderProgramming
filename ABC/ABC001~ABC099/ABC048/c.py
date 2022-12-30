n, x = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(n-1):
    p = a[i]
    q = a[i+1]
    if p+q <= x:
        continue
    if p+q > x:
        ans += p+q-x
        diff = a[i+1]-abs(p+q-x)
        a[i+1] = max(0, a[i+1]-(p+q-x))

print(ans)
