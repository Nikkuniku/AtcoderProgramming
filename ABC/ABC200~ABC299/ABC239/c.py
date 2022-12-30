x1,y1,x2,y2=map(int,input().split())

dx=[1,2,2,1,-1,-2,-2,-1]
dy=[2,1,-1,-2,-2,-1,1,2]

def dist(a,b,c,d):
    return ((a-c)**2 + (b-d)**2)

ans='No'
for i in range(8):
    p=x1+dx[i]
    q=y1+dy[i]
    if dist(p,q,x2,y2)==5:
        ans='Yes'
print(ans)