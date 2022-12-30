n,u,v=map(int,input().split())
edge =[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    a,b = a-1 ,b-1
    edge[a].append(b)
    edge[b].append(a)

    
print(edge)