x, y, n = map(int, input().split())

ans = 10000000
for i in range(n):
    tmp = x*n
    if n-3*i >= 0:
        tmp = y*i + (n-3*i)*x
    ans = min(ans, tmp)
print(ans)
