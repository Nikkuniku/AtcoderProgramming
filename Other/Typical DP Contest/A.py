n=int(input())
p=list(map(int,input().split()))

W=sum(p)

dp=[[False]*(W+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(n+1):
    for w in range(W+1):
        if i>0:
            # p_iを選ぶ
            if dp[i-1][w-p[i-1]]==True:
                dp[i][w]=True
            
            #p_iを選ばない
            if dp[i-1][w]==True:
                dp[i][w]=True


ans=0

for w in range(W+1):
    for i in range(n+1):
        if dp[i][w]==True:
            ans+=1
            break

print(ans)