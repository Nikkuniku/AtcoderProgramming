N,K,C=map(int,input().split())
S=input()
dp=[0]*(N+1)
ep=[0]*(N+1)
for i,v in enumerate(S):
    if v=='o':
        dp[i+1]=max(dp[i+1],dp[max(i+1-C-1,0)]+1,dp[i])
    else:
        dp[i+1]=max(dp[i+1],dp[i])
for i,v in enumerate(S[::-1]):
    if v=='o':
        ep[i+1]=max(ep[i+1],ep[max(i+1-C-1,0)]+1,ep[i])
    else:
        ep[i+1]=max(ep[i+1],ep[i])
ep=ep[::-1]
print(dp)
print(ep)
if dp[-1]>K:
    exit()
ans=[]
for i,v in enumerate(S):
    if v=='o':
        p=dp[max(i+1-C-1,0)]
        q=ep[min(i+1+C+1,N)]
        if p+q==K-1:
            ans.append(i+1)
print(*ans,sep="\n")  