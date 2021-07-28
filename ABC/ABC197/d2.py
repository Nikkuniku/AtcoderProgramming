import math,cmath

n=int(input())
x0,y0=map(int,input().split())
xn,yn=map(int,input().split())

z=cmath.rect(1,math.radians(360/n))

a=complex(x0,y0)
o=complex((x0+xn)/2,(y0+yn)/2)

ans=(a-o)*z+o
print(ans.real,ans.imag)