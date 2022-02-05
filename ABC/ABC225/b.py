n=int(input())
edge=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    edge[a].append(b)
    edge[b].append(a)

ans='No'
for i in range(n):
    if len(edge[i])==n-1:
        ans='Yes'
        break

print(ans)