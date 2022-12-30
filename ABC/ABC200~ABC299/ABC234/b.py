n=int(input())
points=[]
for _ in range(n):
    x,y=map(int,input().split())
    points.append([x,y])

def kyori(p,q):
    return ((p[0]-q[0])**2 + (p[1]-q[1])**2)**0.5

ans=0

for i in range(n):
    for j in range(i+1,n):
        ans = max(ans,kyori(points[i],points[j]))

print(ans)

