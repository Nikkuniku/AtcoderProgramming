n,m,q=map(int,input().split())
goods=[]
for _ in range(n):
    w,v=map(int,input().split())
    goods.append([w,v,0])

goods=sorted(goods,key=lambda x:x[0],reverse=True)
goods=sorted(goods,key=lambda x:x[1],reverse=True)
a=list(map(int,input().split()))
box=[]
for i in range(m):
    box.append([a[i],i+1])

box=sorted(box,key=lambda x :x[0],reverse=True)

for _ in range(q):
    l,r=map(int,input().split())
    ans=0
    for j in range(n):
        goods[j][2]=0

    for i in range(m):
        if l<=box[i][1]<=r:
            continue
        for j in range(n):
            if goods[j][2]==0 and goods[j][0]<=box[j][0]:
                ans+=goods[j][1]
                goods[j][2]=1
                break

    print(ans)