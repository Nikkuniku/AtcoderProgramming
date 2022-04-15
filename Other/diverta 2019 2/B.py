n=int(input())

points=set()
ans=n
for _ in range(n):
    x,y=map(int,input().split())
    points.add((x,y))

points_list=list(points)
for i in range(n):
    x1,y1=points_list[i]
    for j in range(n):
        if i==j:
            continue
        x2,y2=points_list[j]

        p=x2-x1
        q=y2-y1
        tmp=n
        for k in range(n):
            x3,y3=points_list[k]
            if (x3+p,y3+q) in points:
                tmp-=1
        
        ans=min(ans,tmp)

print(ans)
