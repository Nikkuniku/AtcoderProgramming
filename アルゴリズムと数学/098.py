n=int(input())
point=[]
for _ in range(n):
    x,y=map(int,input().split())
    point.append([x,y])
a,b=map(int,input().split())

cnt=0
for i in range(n):
    if i<n-1:
        p1=point[i]
        p2=point[i+1]
    else:
        p1=point[i]
        p2=point[0]
    
    # 上向きの辺と下向きの辺についてチェック
    if p1[1]<=b<p2[1] or p1[1]>b>=p2[1]:
        x=p1[0] + (b-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])

        if a<x:
            cnt+=1


from math import atan2, pi
def inside_polygon1(p0, qs):
    x, y = p0
    L = len(qs)
    theta = 0
    for i in range(L):
        x0, y0 = qs[i-1]; x1, y1 = qs[i]
        x0 -= x; y0 -= y
        x1 -= x; y1 -= y

        cv = x0*x1 + y0*y1
        sv = x0*y1 - x1*y0
        if sv == 0 and cv <= 0:
            # a point is on a segment
            return True

        theta += atan2(sv, cv)
    return abs(theta) > 1

ans='OUTSIDE'
if inside_polygon1([a,b],point):
    ans='INSIDE'
print(ans)