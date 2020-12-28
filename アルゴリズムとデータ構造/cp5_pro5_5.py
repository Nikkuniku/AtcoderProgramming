n=int(input())
a=list(map(int,input().split()))
W=int(input())

dp=[[False]*(W+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(n+1):
    for w in range(W+1):
        if i>0:
            if w-a[i-1]>=0 and dp[i-1][w-a[i-1]]==True:
                dp[i][w]=True
            
            if w-a[i-1]>=0 and dp[i][w-a[i-1]]==True:
                dp[i][w]=True

            if dp[i-1][w]==True:
                dp[i][w]=True


print(*dp,sep="\n")

print(dp[n][W])