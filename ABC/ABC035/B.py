s=input()
t=int(input())

now=[0,0]
hatena=0
for i in range(len(s)):
    if s[i]=='L':
        now[0]-=1
    elif s[i]=='R':
        now[0]+=1
    elif s[i]=='U':
        now[1]+=1
    elif s[i]=='D':
        now[1]-=1
    elif s[i]=='?':
        hatena+=1

dist =abs(now[0]) + abs(now[1])

if t==1:
    dist+=hatena
else:
    if hatena>=dist:
        hatena-=dist
        dist = hatena%2
    else:
        dist=dist-hatena

print(dist)