n = int(input())
s = list(input())


def chr_int(z):
    return ord(z)-97


dp = [[-1]*n for _ in range(26)]

for i in range(n):
    p = chr_int(s[i])
    dp[p][i] = i
    if i+1 < n:
        for j in range(26):
            dp[j][i+1] = dp[j][i]

i = 0
j = n-1
ans = []
while i < j:
    p = s[i]
    flg = False
    for k in range(chr_int(p)):
        if dp[k][j] != -1 and i < dp[k][j]:
            ans.append((i, dp[k][j]))
            j = dp[k][j]-1
            flg = True
            break

    i += 1
for c in ans:
    a, b = c
    s[a], s[b] = s[b], s[a]
print(''.join(s))
