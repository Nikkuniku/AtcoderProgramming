n,m=map(int,input().split())

dp=[0]*n
deg=[0]*n
edge=[[] for _ in range(n)]

for _ in range(m):
    x,y=map(int,input().split())
    # x,y=x-1,y-1

    deg[y]+=1

    edge[x].append(y)


from collections import deque
q=deque([])

for i in range(n):
    if deg[i]==0:
        q.append(i)


ans=[]
while q:
    now = q.popleft()
    ans.append(now)
    for e in edge[now]:
        deg[e]-=1
        dp[e]=max(dp[now]+1,dp[e])

        if deg[e]==0:
            q.append(e)

# print(max(dp))
for j in range(len(ans)):
    print(ans[j])