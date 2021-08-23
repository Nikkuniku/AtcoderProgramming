r,c=map(int,input().split())
senbei=[tuple(map(int,input().split())) for _ in range(r)]

p = [0]*c

for i in range(r):
    for j in range(c):
        if senbei[i][j]==0:
            p[j]+=1
ans=0
for i in range(1<<r):
    tmp=0
    rev =p.copy()

    for j in range(r):
        if (i>>j)&1:
            for k in range(c):
                if senbei[j][k]==0:
                    rev[k]-=1
                else:
                    rev[k]+=1
    
    for k in range(c):
        tmp+=max(rev[k],r-rev[k])

    ans=max(ans,tmp)
print(ans)