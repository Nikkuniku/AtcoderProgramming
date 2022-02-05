from collections import deque
x=list(input())
x=deque(map(int,x))
n=len(x)
for j in range(1,n):
    x[j]+=x[j-1]

answer=deque([])
c=0
for k in range(n-1,-1,-1):
    tmp=x[k]
    c,mod=divmod(tmp+c,10)
    answer.appendleft(str(mod))

if c!=0:
    answer.appendleft(str(c))
print(''.join(answer))