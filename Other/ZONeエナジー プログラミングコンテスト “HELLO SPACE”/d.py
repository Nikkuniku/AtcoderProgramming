from collections import deque
s=list(input())
t=deque()

flg=1
for i in range(len(s)):
    if s[i]=='R':
        flg*=-1
    else:
        if flg>0:
            if t and t[-1]==s[i]:
                t.pop()
            else:
                t.append(s[i])
        else:
            if t and t[0]==s[i]:
                t.popleft()
            else:
                t.appendleft(s[i])
if flg<0:
    t=reversed(t)
print(''.join(t))
