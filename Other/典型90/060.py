n=int(input())
a=list(map(int,input().split()))
INF=10**18
dp0=[INF]*(n+1)
dp1=[INF]*(n+1)

s0=[]
s1=[]
import bisect
cur0=0
cur1=0
for i in range(n):
    k=bisect.bisect_left(dp0,a[i])
    dp0[k]=a[i]
    cur0=max(k+1,cur0)
    s0.append(cur0)

    j=bisect.bisect_left(dp1,a[n-1-i])
    dp1[j]=a[n-1-i]
    cur1=max(j+1,cur1)
    s1.append(cur1)
s1=list(reversed(s1))
ans=0
for i in range(len(s1)):
    ans=max(ans,s0[i]+s1[i]-1)
print(ans)