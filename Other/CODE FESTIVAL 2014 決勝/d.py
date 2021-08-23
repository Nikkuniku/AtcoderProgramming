a=int(input())
n=1000
dp=[[0]*n for _ in range(n)]
dp[0][0]=1

for i in range(n):
    for j in range(n):
        if 0<=j+1<n:
            dp[i][j+1]+=dp[i][j]
            if 0<=i+1<n:
                dp[i+1][j+1]+=dp[i][j]
d={}
for p in range(n):
    for q in range(n):
        d[dp[p][q]]=(q+1,p)
ans=(-1,-1)
if a in d:
    ans=d[a]
print(*ans)