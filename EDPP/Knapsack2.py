N,W=map(int,input().split())



V_max = 0
# 価値の最大値を求める
Weights=[]
Values=[]
for i in range(N):
    w_i,v_i = map(int,input().split())
    Weights.append(w_i)
    Values.append(v_i)
    V_max=max(V_max,v_i)

# print(*Data,sep="\n")
# print(V_max)

NV = N*V_max
#DPテーブル
dp=[]
for k in range(N+1):
    dp.append([float('inf')]*( NV + 1 ))
dp[0][0]=0

# print(*dp,sep="\n")

for i in range(N):
    for v in range(NV+1):
        if v - Values[i] >= 0:
            dp[i+1][v] = min( dp[i][v] , dp[i][v-Values[i]] + Weights[i] )
        else:
            dp[i+1][v] = dp[i][v]

# print(*dp,sep="\n")
dp[N].reverse()

# print(dp[N])
print([NV-dp[N].index(l) for l in dp[N] if l<=W][0])