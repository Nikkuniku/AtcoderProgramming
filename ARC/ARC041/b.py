n,m=map(int,input().split())
ameba=[[0]*(m+2)]
for _ in range(n):
    p=[0]+list(map(int,input()))+[0]
    ameba.append(p)
ameba.append([0]*(m+2))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
ans=[[0]*(m+2) for _ in range(n+2)]
for i in range(1,n+1):
    for j in range(1,m+1):
        flg=0
        tmp=20
        for k in range(4):
            x=i+dx[k]
            y=j+dy[k]
            if ameba[x][y]>0:
                flg+=1
                tmp=min(tmp,ameba[x][y])
        
        if flg==4:
            for k in range(4):
                x=i+dx[k]
                y=j+dy[k]
                ameba[x][y]-=tmp
            
            ans[i][j]+=tmp

for c in ans[1:n+1]:
    tmp=''
    for q in c[1:m+1]:
        tmp+=str(q)
    print(tmp)
    