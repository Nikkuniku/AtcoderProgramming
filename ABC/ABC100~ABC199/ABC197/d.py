n=int(input())
x0,y0=map(int,input().split())
xn,yn=map(int,input().split())

mx=(x0+xn)/2
my=(y0+yn)/2
from math import radians,sin,cos
theta=radians(360/n)

ans_x=mx+(x0-mx)*cos(theta)-(y0-my)*sin(theta)
ans_y=my+(x0-mx)*sin(theta)+(y0-my)*cos(theta)

print(ans_x,ans_y)