t=int(input())
l,X,Y=map(int,input().split())
q=int(input())

import math 
def now(e):
    x=0
    y = -l*math.sin((2*e*math.pi)/(t))/2
    z = -l*math.cos((2*e*math.pi)/(t))/2 + l/2

    return [x,y,z]

def dist(place):
    bottom = math.sqrt((X-place[0])**2 + (Y-place[1])**2)
    return bottom

ans=[]
for _ in range(q):
    e_i =int(input())
    theta = math.atan(now(e_i)[2]/dist(now(e_i))) *180 /math.pi
    ans.append(theta)

for i in range(len(ans)):
    print(ans[i])