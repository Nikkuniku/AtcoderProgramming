n=int(input())
from itertools import groupby
from collections import deque
s=list(input())
gr=groupby(s)
#flg=0:白の状態
flg=0
black=[]
white=[]
for k,v in gr:
    if flg==0 and k=='#':
        flg=1
        black.append(len(list(v)))
    elif flg==1:
        if k=='#':
            black.append(len(list(v)))
        else:
            white.append(len(list(v)))
if len(black)==0 or len(white)==0:
    print(0)
    exit(0)

ans=white.copy()
cnt=sum(ans)

white=deque(white)
black=deque(black)
ans=deque(ans)

while white:
    ans.popleft()
    white.popleft()
    ans.append(black.popleft())
    cnt=min(cnt,sum(ans))

print(cnt)



