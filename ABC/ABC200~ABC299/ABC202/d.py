a,b,k=map(int,input().split())
import math
s=math.factorial(a+b)//(math.factorial(a)*math.factorial(b))
from collections import deque
q=deque()
d={}
d['a']=0
d['b']=0
for _ in range(a):
    q.appendleft('a')
    d['a']+=1
for _ in range(b):
    q.append('b')
    d['b']+=1

l=1
r=s
ans=''
while q:
    a_n=d['a']
    b_n=d['b']
    mid =(b_n*l+a_n*r)//(a_n+b_n)
    if mid<k:
        ans+=q.pop()
        d['b']-=1
        l=mid
    else:
        ans+=q.popleft()
        d['a']-=1
        r=mid
print(ans)