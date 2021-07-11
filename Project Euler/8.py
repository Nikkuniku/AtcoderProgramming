n=int(input())
arr=[]
for _ in range(20):
    p=[int(i) for i in list(input())]
    arr+=p

from collections import deque
d=deque([])

ans=1
for i in range(len(arr)):
    if len(d)<n:
        d.append(arr[i])

    if len(d)==n:
        tmp=1
        for j in range(len(d)):
            tmp*=d[j]
        
        ans=max(ans,tmp)
        d.popleft()

print(ans)

        