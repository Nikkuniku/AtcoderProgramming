from collections import deque
s=deque(input())
cnt=0
while s:
    if s[-1]=='a':
        s.pop()
        cnt+=1
    else:
        break
while s:
    if s[0]=='a':
        s.popleft()
        cnt-=1
    else:
        break

n=len(s)
ans='Yes'
s=list(s)
l=s[::-1]
if s!=l or cnt<0:
    ans='No'
print(ans)