import sys
def input():
    return sys.stdin.readline()[:-1]
mx=5000
n,k=map(int,input().split())
dp=[[0]*(mx+2) for _ in range(mx+2)]
for i in range(n):
    a,b=map(int,input().split())
    dp[a][b]+=1

# 行方向
for x in range(mx+1):
    for y in range(mx):
        dp[x][y+1]+=dp[x][y]
for x in range(mx+1):
    for y in range(mx):
        dp[x+1][y]+=dp[x][y]
ans=0
for i in range(1,mx+2-k):
    for j in range(1,mx+2-k):
        a=i
        b=i+k
        c=j
        d=j+k
        p=dp[b][d]-dp[b][c-1]-dp[a-1][d]+dp[a-1][c-1]
        if ans<p:ans=p
print(ans)