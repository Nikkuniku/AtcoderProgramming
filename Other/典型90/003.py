n=int(input())
edge=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)

from collections import deque
q=deque()

# # 第一ステップ
dist1= [-1]*n
dist1[0]=0
q.append(0)
while q:
    v=q.popleft()

    for e in edge[v]:
        if dist1[e]==-1:
            dist1[e] = dist1[v]+1
            q.append(e)

# # 第2ステップ
dist2= [-1]*n
v= dist1.index(max(dist1))
dist2[v]=0
q.append(v)
while q:
    v=q.popleft()

    for e in edge[v]:
        if dist2[e]==-1:
            dist2[e] = dist2[v]+1
            q.append(e)

ans=max(dist2)+1

print(ans)
