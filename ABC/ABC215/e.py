n=int(input())
S=input()
mod=998244353

dp=[[[0]*10 for _ in range(1<<10)] for _ in range(n+1)]
d={
    'A':0
    ,'B':1
    ,'C':2
    ,'D':3
    ,'E':4
    ,'F':5
    ,'G':6
    ,'H':7
    ,'I':8
    ,'J':9
}
for i in range(n):
    x=d[S[i]]
    for s in range(1<<10):
        for j in range(10):
            # i回目のコンテストに参加しない
            dp[i+1][s][j]+=dp[i][s][j]
            dp[i+1][s][j]%=mod
            # i回目のコンテストに参加する場合
            if j==x:
                dp[i+1][s][j]+=dp[i][s][j]
                dp[i+1][s][j]%=mod
    # まだi回目のコンテストに参加したことがない
    for s in range(1<<10):
        if s&(1<<x):
            continue
        for j in range(10):
                dp[i+1][s|(1<<x)][x]+=dp[i][s][j]            
                dp[i+1][s|( 1<<x)][x]%=mod
    
    dp[i+1][1<<x][x]+=1
    dp[i+1][1<<x][x]%=mod
ans=0
for v in range(1<<10):
    for j in range(10):
        ans+=dp[n][v][j]

print(ans%mod)