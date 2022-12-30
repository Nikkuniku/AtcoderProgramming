N, S = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(N)]
dp = [[False]*(S+1) for _ in range(N+1)]
dp[0][0] = True
for i in range(N):
    a, b = cards[i]
    for s in range(S+1):
        if s-a >= 0:
            dp[i+1][s] |= dp[i][s-a]
        if s-b >= 0:
            dp[i+1][s] |= dp[i][s-b]

if not dp[N][S]:
    print('No')
    exit()

i = N
j = S
ans = []
while i > 0 and j > 0:
    a, b = cards[i-1]
    if dp[i-1][j-a]:
        ans.append('H')
        i -= 1
        j -= a
    elif dp[i-1][j-b]:
        ans.append('T')
        i -= 1
        j -= b
print('Yes')
print(''.join(ans[::-1]))
