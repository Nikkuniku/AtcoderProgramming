from re import A


points=[]
for _ in range(3):
    x,y=map(int,input().split())
    points.append([x,y])
points.sort()

p=points[0][0]
q=points[1][0]
r=points[2][0]
if p==q:
    x=r
    for y in [points[0][1],points[1][1]]:
        s=(x-p)*(y-points[2][1])
        if s!=0:
            ans=s
            break
else:
    x=p
    for y in [points[1][1],points[2][1]]:
        s=(x-q)*(y-points[0][1])
        if s!=0:
            ans=s
            break
print(x,y)
