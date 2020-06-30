h,w=map(int,input().split())
n=int(input())
a=list(map(int,input().split()))

from collections import deque

d=deque([])
for i in range(n):
    number=i+1
    cnt=a[i]
    for _ in range(cnt):
        d.append(number)

ans=[[0]*w for _ in range(h)]

flg_h=0
i=0
j=0
while d:
    v=d.popleft()
    ans[i][j]=v
    if flg_h==0:
        if i<h-1:
            i+=1
        else:
            j+=1
            flg_h=1
    elif flg_h==1:
        if i>0:
            i-=1
        else:
            j+=1
            flg_h=0

for i in range(h):
    print(*ans[i])