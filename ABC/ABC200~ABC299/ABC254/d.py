n = int(input())

ans = 0
for i in range(1, n+1):
    k = i
    for d in range(2, n+1):
        if d**2 > k:
            break
        while k % (d**2) == 0:
            k //= d**2
    for d in range(1, n+1):
        if k*(d**2) <= n:
            ans += 1
        else:
            break

print(ans)
