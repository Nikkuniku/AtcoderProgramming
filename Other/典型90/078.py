n,m=map(int,input().split())
node=[0]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    node[max(a,b)]+=1

ans=0
for i in range(1,n+1):
    if node[i]==1:
        ans+=1

print(ans)