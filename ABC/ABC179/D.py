n,k=map(int,input().split())

dp=[0]*(n+1)

for _ in range(k):
    l,r=map(int,input().split())

    now=0
    for i in range(l,r+1):
        dp[now+i]+=1