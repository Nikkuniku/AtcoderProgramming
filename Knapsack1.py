N,W=map(int,input().split())

# dp用配列
dp=[]
for k in range(N+1):
    dp.append([0]*(W+1))


for i in range(N):
    w_i,v_i = map(int,input().split())
    for w in range(W+1):
        if w>=w_i:
            dp[i+1][w] = max(dp[i][w-w_i] + v_i , dp[i][w])
        else:
            dp[i+1][w] =dp[i][w]

# print(*dp,sep="\n")

print(dp[N][W])
        
