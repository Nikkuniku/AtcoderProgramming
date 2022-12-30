s=input()
k=int(input())
a=[]
ans=0
for i in range(len(s)):
    if s[i]=='X':
        a.append(1)
    else:
        a.append(-1)

from collections import deque
q=deque()
cnt=0
for c in a:
    q.append(c)
    # '.'の時はコストがかかったとする
    if c<0:
        cnt+=1

    while q and cnt>k:
        v=q.popleft()
        if v<0:
            cnt-=1

    ans=max(ans,len(q))

print(ans)