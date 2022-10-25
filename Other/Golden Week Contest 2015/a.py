s = [25, 39, 51, 76, 163, 111, 128, 133, 138]
g = [58, 136]
dp = [[False]*(sum(s)+2) for _ in range(len(s)+1)]
dp[0][0] = True

for i in range(len(s)):
    for j in range(sum(s)+1):
        dp[i+1][j] |= dp[i][j]
        if j-s[i] >= 0:
            dp[i+1][j] |= dp[i][j-s[i]]
tmp = []
for w in range(sum(s)+2):
    if dp[len(s)][w]:
        tmp.append(w)
ans = []
for i in g:
    for t in tmp:
        ans.append(t+i)
ans += tmp
ans = list(set(ans))
ans.sort()
print(*ans, sep="\n")
