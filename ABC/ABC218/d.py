n=int(input())
point=[]
s_point=set()
d={}

for i in range(n):
    x,y=map(int,input().split())
    point.append([i,x,y])
    s_point.add((x,y))
    d[(x,y)]=i 


rectangles=set()

for j in range(n):
    for k in range(j+1,n):
        a=point[j]
        b=point[k]

        ax=a[1]
        ay=a[2]

        bx=b[1]
        by=b[2]

        if ax!=bx and ay!=by:
            if (ax,by) in s_point and (bx,ay) in s_point:
                ans=tuple(sorted((a[0],b[0],d[(ax,by)],d[(bx,ay)]),key=lambda x:x))
                rectangles.add(ans)
print(len(rectangles))
