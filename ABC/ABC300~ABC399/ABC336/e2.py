def isOK(n):
    k = n
    d_n = 0
    while k > 0:
        d_n += k % 10
        k //= 10
    return n % d_n == 0


N = 10000
ans = 0
for i in range(1, N + 1):
    ans += isOK(i)
print(ans)
