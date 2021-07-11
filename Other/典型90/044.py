n,q=map(int,input().split())
from collections import deque

a=deque(map(int,input().split()))
shift=0
for _ in range(q):
    t,x,y = map(int,input().split())
    x,y=x-1,y-1
    if t==1:
        a[(x+shift)%n],a[(y+shift)%n]=a[(y+shift)%n],a[(x+shift)%n]
    elif t==2:
        shift = (shift+n-1)%n
    else:
        print(a[(x+shift)%n])
