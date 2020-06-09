N,K=map(int,input().split())
H=list(map(int,input().split()))

dp = [float('inf')]*(N+1)
dp[0]=0
dp[1]=0
    

for i in range(N):
    if i!=0:
        for k in range(K):
            if i-k>=1:
                dp[i+1] = min ( dp[i+1] ,dp[i-k] + abs(H[i]-H[i-(k+1)]) )
print(int(dp[N]))
# print(dp)