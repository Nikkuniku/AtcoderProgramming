n, m = map(int, input().split())
edge=[set() for _ in range(n+1)]
vertex=[i+1 for i in range(n)]
for _ in range(m):
    a,b=map(int,input().split())
    edge[a].add(b)    
    edge[b].add(a)    
    
from itertools import permutations
pe=permutations(vertex)

ans=0
for p in pe:
    if p[0]!=1:
        continue
    Flg=True
    for i in range(n-1):
        if p[i+1] in edge[p[i]]:
            continue
        else:
            Flg=False
            break
    
    if not Flg:
        continue
    ans+=1

print(ans)
        