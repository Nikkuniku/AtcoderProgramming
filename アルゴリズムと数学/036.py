from math import pi,cos,sin

a,b,h,m=map(int,input().split())

theta = (h/6 + m/360)*pi
phai = m*pi/30

hour=(a*cos(theta),a*sin(theta))
minute=(b*cos(phai),b*sin(phai))

ans_vec=(hour[0]-minute[0],hour[1]-minute[1])
ans=(ans_vec[0]**2 +ans_vec[1]**2)**0.5
print(ans)