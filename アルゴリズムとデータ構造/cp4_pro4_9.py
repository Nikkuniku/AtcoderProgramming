n=int(input())
a=list(map(int,input().split()))
W=int(input())

dp=[[False]*(W+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(1,n+1):
    for w in range(W+1):
        
        if dp[i-1][w-a[i-1]]:
            dp[i][w]=True
        
        if dp[i-1][w]:
            dp[i][w]=True

        
if dp[n][W]:
    print('Yes')
else:
    print('No')