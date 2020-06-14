n=int(input())
s=input()

if n%2==0:
    print(-1)
    exit(0)

from collections import deque

ans = deque(['b'])
ans_s = ''.join(ans)
if s==ans_s:
    print(0)
    exit(0)

i=1
while i<=101:
    if i%3==1:
        ans.appendleft('a')
        ans.append('c')
    elif i%3==2:
        ans.appendleft('c')
        ans.append('a')
    else:
        ans.appendleft('b')
        ans.append('b')

    ans_s = ''.join(ans)

    if ans_s ==s:
        print(i)
        exit(0)
    i+=1

print(-1)