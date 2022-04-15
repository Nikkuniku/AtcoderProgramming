n,d=map(int,input().split())
wall=[]
for _ in range(n):
    wall.append(list(map(int,input().split())))

wall.sort(key=lambda x:x[1])

ans=0
r=wall[0][1]
i=1
while i<n:
    l=wall[i][0]
    if l<=r+d-1:
        i=i
    else:
        ans+=1
        r=wall[i][1]
    i+=1
ans+=1
print(ans)