n=int(input())
s=input()

from collections import deque

d=deque([])
for i in range(n):
    d.append(s[i])

    if len(d)>=3:
        if d[-3]=='f' and d[-2]=='o' and d[-1]=='x':
            d.pop()
            d.pop()
            d.pop()

print(len(d))

