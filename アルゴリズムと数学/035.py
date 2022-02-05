x1, y1, r1 = map(int, input().split())
x2, y2, r2 = map(int, input().split())


# r2は大きい円にする
if r1 > r2:
    x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1
c1 = [x1, y1]
c2 = [x2, y2]

def kyori(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

ans=3
d=kyori(c1,c2)
if d<r2-r1:
    ans=1
elif d==r2-r1:
    ans=2
elif d==r1+r2:
    ans=4
elif d>r1+r2:
    ans=5
print(ans)