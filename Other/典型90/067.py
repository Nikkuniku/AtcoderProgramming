n,k=map(int,input().split())
n=list(str(n))

from collections import deque
for _ in range(k):
    tmp=0
    for j in range(len(n)-1,-1,-1):
        tmp+=int(n[j])*pow(8,len(n)-1-j)
    n=deque([])
    while True:
        p=tmp//9
        q=str(tmp%9)
        if q=='8':
            n.appendleft('5')
        else:
            n.appendleft(q)

        tmp//=9
        if p==0:
            break

print(''.join(n))