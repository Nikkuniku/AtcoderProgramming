n, L, R = map(int, input().split())
a = list(map(int, input().split()))
INF = 10**18
f = [INF]*(n+1)
g = [INF]*(n+1)
f[0] = 0
g[-1] = 0
for i in range(1, n+1):
    f[i] = min(f[i-1]+a[i-1], L*i)
for i in range(1, n+1):
    g[n-i] = min(g[n-i+1]+a[n-i], R*i)
ans = INF
for i in range(len(f)):
    ans = min(ans, f[i]+g[i])
print(ans)
