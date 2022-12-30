from collections import defaultdict
N = int(input())
d = defaultdict(list)
for _ in range(N):
    x, c = map(int, input().split())
    d[c].append(x)

colors = defaultdict(int)
Color = []
INF = 1 << 62
for k, v in d.items():
    colors[k] = [min(v), max(v)]
    Color.append((k, colors[k]))
Color.append((0, [0, 0]))
Color.append((INF, [0, 0]))
Color.sort()
M = len(Color)
dp = [[INF]*2 for _ in range(M+1)]
dp[0] = [0, 0]
ans = 0
for i in range(M-1):
    dp[i+1][0] = min(dp[i+1][0], dp[i][0]+abs(Color[i+1][1][0]-Color[i][1][1]))
    dp[i+1][0] = min(dp[i+1][0], dp[i][1]+abs(Color[i+1][1][0]-Color[i][1][0]))

    dp[i+1][1] = min(dp[i+1][1], dp[i][0]+abs(Color[i+1][1][1]-Color[i][1][1]))
    dp[i+1][1] = min(dp[i+1][1], dp[i][1]+abs(Color[i+1][1][1]-Color[i][1][0]))
    ans += max(Color[i][1])-min(Color[i][1])

ans += min(dp[M-1])
print(ans)
