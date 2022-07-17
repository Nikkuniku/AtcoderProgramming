n, K = map(int, input().split())

ls = [0]*(n+1)
rs = [0]*(n+1)
v = [0]*(n+1)
for i in range(K):
    c, k = input().split()
    k = int(k)
    if c == 'L':
        ls[k] = 1
    else:
        rs[k] = 1
    v[k] = i+1

for i in range(n):
    rs[i+1] += rs[i]
    ls[n-(i+1)] += ls[n-i]
ans = 1
MOD = 998244353
for i in range(1, n+1):
    if v[i] > 0:
        continue
    ans *= K-ls[i]-rs[i]
    ans %= MOD
print(ans)
