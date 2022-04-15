n=int(input())
s=list(input())
from collections import deque

d=deque([n])

for i in range(n-1,-1,-1):
    if s[i]=='R':
        d.appendleft(i)
    else:
        d.append(i)

print(*d)