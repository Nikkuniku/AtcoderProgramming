n, k = map(int, input().split())
ans = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if 1 <= k-a-b <= n:
            ans += 1
print(ans)
