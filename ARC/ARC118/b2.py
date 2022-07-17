k, n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = 0
for i in range(k):
    tmp = abs((b[i]/m)-(a[i]/n))
    ans = max(ans, tmp)

print(ans)
print(ans*n*m)
