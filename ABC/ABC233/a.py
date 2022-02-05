x,y=map(int,input().split())
from math import ceil

t=ceil((y-x)/10)
ans=max(0,t)
print(ans)