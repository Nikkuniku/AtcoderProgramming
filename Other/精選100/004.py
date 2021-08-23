n,m=map(int,input().split())
point=[tuple(map(int,input().split())) for _ in range(n)]

ans=0
for i in range(m-1):
    for j in range(i+1,m):   
        tmp=0
        for k in range(n):
            tmp+=max(point[k][i],point[k][j])
        
        ans=max(ans,tmp)
print(ans)