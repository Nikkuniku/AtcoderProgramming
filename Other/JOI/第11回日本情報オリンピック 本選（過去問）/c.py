N, T, S = map(int, input().split())
shop = [list(map(int, input().split())) for _ in range(N)]
dp1_1 = [0]*(S+1)
dp2_1 = [0]*(T-S+1)
dp1i = [0]*(N+1)
dpiN = [0]*(N+1)
# 1~i
for i in range(N):
    dp1_2 = [0]*(S+1)
    a, b = shop[i]
    for t in range(S+1):
        # 遊ばない
        dp1_2[t] = max(dp1_2[t], dp1_1[t])
        if t-b >= 0:
            dp1_2[t] = max(dp1_2[t], dp1_1[t-b]+a)
    dp1_1 = dp1_2
    dp1i[i+1] = dp1_1[S]
# i~N
for i in range(N-1, -1, -1):
    dp2_2 = [0]*(T-S+1)
    a, b = shop[i]
    for t in range(T-S+1):
        dp2_2[t] = max(dp2_2[t], dp2_1[t])
        if t-b >= 0:
            dp2_2[t] = max(dp2_2[t], dp2_1[t-b]+a)
    dp2_1 = dp2_2
    dpiN[i] = dp2_1[T-S]
ans = 0
for k in range(1, N+1):
    tmp = dp1i[k]+dpiN[k]
    ans = max(ans, tmp)
print(ans)
