N,W=map(int,input().split())

w,value=[],[]

for _ in range(N):
    w_i,v_i=map(int,input().split())

    w.append(w_i)
    value.append(v_i)

INF=10**9
V=sum(value)

dp=[[INF]*(V+1) for _ in range(N+1)]
dp[0][0]=0

for i in range(1,N+1):
    for v in range(V+1):

        if v-value[i-1]>=0:
            dp[i][v]=min(dp[i-1][v-value[i-1]]+w[i-1],dp[i-1][v])
        else:
            dp[i][v]=min(dp[i-1][v],dp[i][v])

for j in range(V+1):
    if dp[N][V-j]<=W:
        ans=V-j
        break


print(ans)