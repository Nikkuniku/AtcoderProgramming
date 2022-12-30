from math import atan,cos,sin
a,b=map(int,input().split())
if a!=0:
    theta = atan(b/a)
    x=cos(theta)
    y=sin(theta)
else:
    x=0
    y=1
print(x,y)