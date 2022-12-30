n, k = map(int, input().split())
ans = 0
for b in range(k+1, n+1):
    p = n//b
    ans += (b-k)*p
    q = n % b
    if q == 0:
        continue
    else:
        if k == 0:
            ans += q
        else:
            ans += max(q-k+1, 0)
print(ans)
