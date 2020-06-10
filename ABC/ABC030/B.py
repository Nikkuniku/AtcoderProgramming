n,m=map(int,input().split())

from math import sin,cos,pi,acos,degrees

rad_long = (m/30) * pi

rad_short = ((n/6) + (m/360))*pi

short = [cos(rad_short),sin(rad_short)]
long =[cos(rad_long),sin(rad_long)]

product =short[0]*long[0] + short[1]*long[1]


print(degrees(acos(product)))