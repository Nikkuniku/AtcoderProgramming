n,m=map(int,input().split())
cnt=[0]*(n+1)
mem=[]
place=[[] for _ in range(n+1)]
for p in range(m):
    k=int(input())
    a=list(map(int,input().split()))
    mem.append(a)
    for j in range(k):
        place[a[j]].append(p)

    cnt[a[-1]]+=1
from collections import deque
q=deque([])
for i in range(n+1):
    if cnt[i]==2:
        q.append(i)
while q:
    v=q.popleft()
    for e in place[v]:
        mem[e].pop()
        if mem[e]:
            cnt[mem[e][-1]]+=1
            if cnt[mem[e][-1]]==2:
                q.append(mem[e][-1])

ans='Yes'
for p in mem:
    if p:
        ans='No'
        break
print(ans)
