n=int(input())
a=[]
for _ in range(n):
    a.append(int(input()))

a=sorted(a)

from collections import deque

d=deque(a)

ans=deque([d.pop()])

for i in range(n-1):
    if i%2==0:
        p=d.popleft()
    else:
        p=d.pop()
        
    if abs(p-ans[0])>=abs(p-ans[-1]):
        ans.appendleft(p)
    else:
        ans.append(p)


dif = 0

for j in range(n-1):
    dif += abs(ans[j+1] - ans[j])

d=deque(a)
ans=deque([])

for i in range(n):
    if i==n-1:
        z=d.pop()

        if abs(z-ans[0])>abs(z-ans[-1]):
            ans.appendleft(z)
        else:
            ans.append(z)
    else:
        if i%2==0:
            p=d.pop()
            ans.append(p)
        else:
            q=d.popleft()
            ans.append(q)

dif2 = 0
for j in range(n-1):
    dif2 += abs(ans[j+1] - ans[j])

print(max(dif,dif2))