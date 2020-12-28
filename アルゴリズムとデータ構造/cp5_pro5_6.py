n=int(input())
a=list(map(int,input().split()))
m=list(map(int,input().split()))
W=int(input())

dp=[[-1]*(W+1) for _ in range(n+1)]
for i in range(n+1):
    dp[i][0]=0

for i in range(n+1):
    for w in range(W+1):
        if i>0:
            if dp[i-1][w]>=0:
                dp[i][w]=m[i-1]
            elif w<a[i-1] or dp[i][w-a[i-1]]<0:
                dp[i][w]=-1
            else:
                dp[i][w]=dp[i][w-a[i-1]]-1

# print(*dp,sep="\n")

z=dp[n][W]

if z>=0:
    ans='Yes'
else:
    ans='No'

print(ans)

