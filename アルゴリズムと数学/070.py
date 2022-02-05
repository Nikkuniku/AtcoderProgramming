n,K=map(int,input().split())
X=[]
Y=[]
for _ in range(n):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

def count_points(lx,rx,dy,uy):
    cnt=0
    for i in range(n):
        px=X[i]
        py=Y[i]
        if lx<=px<=rx and dy<=py<=uy:
            cnt+=1
    return cnt

ans=10**19
for i in range(n):
    for j in range(n):
        for k in range(n):
            for m in range(n):
                lx=X[i]
                rx=X[j]
                dy=Y[k]
                uy=Y[m]
                if lx<rx and dy<uy:
                    if count_points(lx,rx,dy,uy)>=K:
                        s=(rx-lx)*(uy-dy)
                        ans=min(ans,s)
print(ans)