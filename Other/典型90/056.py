n,s=map(int,input().split())
a,b=[],[]
for _ in range(n):
    a_i,b_i=map(int,input().split())
    a.append(a_i)
    b.append(b_i)

dp=[[False]*(s+1) for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    for j in range(s+1):
        dp[i+1][j]= dp[i+1][j] 
        if j-a[i]>=0:
            dp[i+1][j]= dp[i+1][j] | dp[i][j-a[i]]
        if j-b[i]>=0:
            dp[i+1][j]= dp[i+1][j] | dp[i][j-b[i]]

ans=dp[n][s]
answer=''
if ans:
    for i in range(n-1,-1,-1):
        if s-a[i]>=0 and dp[i][s-a[i]]:
            answer='A'+answer
            s-=a[i]
        elif s-b[i]>=0 and dp[i][s-b[i]]:
            answer='B'+answer
            s-=b[i]
else:
    answer='Impossible'

print(answer)
