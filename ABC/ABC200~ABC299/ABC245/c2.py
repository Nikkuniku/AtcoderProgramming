n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

dp=[False]*(n)
ep=[False]*(n)
dp[0]=True
ep[0]=True

for i in range(n-1):
    if dp[i] and abs(a[i+1]-a[i])<=k:
        dp[i+1]=True
    if ep[i] and abs(a[i+1]-b[i])<=k:
        dp[i+1]=True
    if ep[i] and abs(b[i+1]-b[i])<=k:
        ep[i+1]=True
    if dp[i] and abs(b[i+1]-a[i])<=k:
        ep[i+1]=True

ans='No'
if dp[n-1] or ep[n-1]:
    ans='Yes'
print(ans)