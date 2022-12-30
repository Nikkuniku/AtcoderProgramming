from math import log2, ceil
n = int(input())
dp = ['' for _ in range(n+1)]
dp[0] = '{}'
for i in range(1, n+1):
    tmp = '{'
    arr = []
    for j in range(ceil(log2(i))+1):
        if i & (1 << j):
            arr.append(dp[j])
    tmp += ','.join(arr)+'}'
    dp[i] = tmp
print(dp[n])
