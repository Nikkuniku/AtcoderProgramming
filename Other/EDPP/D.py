n,W=map(int,input().split())
w,v=[],[]

for _ in range(n):
    w_i,v_i=map(int,input().split())
    
    w.append(w_i)
    v.append(v_i)

dp=[[0 for _ in range(W+1)] for _ in range(n+1)]


for i in range(n+1):
    for p in range(W+1):
        if i>0 :

            if p-w[i-1]>=0:
                dp[i][p]=max(dp[i-1][p],dp[i-1][p-w[i-1]]+v[i-1])
            
            dp[i][p]=max(dp[i-1][p],dp[i][p])


print(dp[n][W])