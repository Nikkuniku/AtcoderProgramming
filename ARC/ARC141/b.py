from itertools import combinations
n, m = map(int, input().split())
a = []
L = -1
MOD = 998244353
for i in range(62):
    if (m >> i) & 1:
        L = i
for i in range(L+1):
    if i == 0:
        a.append(1)
    elif i < L:
        a.append(pow(2, i+1)-pow(2, i))
    elif i == L:
        a.append(m-pow(2, i)+1)
if n > 60:
    print(0)
    exit()
r = min(60, n)
k = len(a)
dp = [[0]*(62) for _ in range(62)]
for i in range(k+1):
    dp[i][0] = 1
for i in range(k):
    for j in range(1, k+1):
        dp[i+1][j] = dp[i][j]+dp[i][j-1]*a[i]
        dp[i+1][j] %= MOD
ans = dp[k][r]
print(ans)
