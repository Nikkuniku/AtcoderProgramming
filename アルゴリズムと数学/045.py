n,m=map(int,input().split())
edge=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    if a>b:
        a,b=b,a
    
    edge[b].append(a)

ans=0
for i in range(len(edge)):
    if len(edge[i])==1:
        ans+=1

print(ans)