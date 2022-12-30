N, T = map(int, input().split())
dish = [list(map(int, input().split())) for _ in range(N)]
dp1 = [[0]*T for _ in range(N+1)]
dp2 = [[0]*T for _ in range(N+1)]
# 1~iまでの料理の満足度
for i in range(N):
    a, b = dish[i]
    for t in range(T):
        dp1[i+1][t] = max(dp1[i+1][t], dp1[i][t])
        if t-a >= 0:
            dp1[i+1][t] = max(dp1[i+1][t], dp1[i][t-a]+b)

for i in range(N-1, -1, -1):
    a, b = dish[i]
    for t in range(T):
        dp2[i][t] = max(dp2[i][t], dp2[i+1][t])
        if t-a >= 0:
            dp2[i][t] = max(dp2[i][t], dp2[i+1][t-a]+b)

ans = 0
for i in range(N):
    for t in range(T):
        tmp = dp1[i][t]+dp2[i+1][T-1-t]+dish[i][1]
        ans = max(ans, tmp)
print(ans)
