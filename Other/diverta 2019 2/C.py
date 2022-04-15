n=int(input())
lb=0
ra=0
ba=0
ans=0

import re

for _ in range(n):
    s=input()

    ans+=s.count('AB')

    if s[0]=='B' and s[-1]=='A':
        ba+=1
    elif s[0]=='B':
        lb+=1
    elif s[-1]=='A':
        ra+=1

if ba>0:
    ans+=ba-1
    ba=1

tmp=min(lb,ra,ba)
ans += 2*tmp

lb-=tmp
ra-=tmp
ba-=tmp

if lb<0:
    lb=0
if ra<0:
    ra=0
if ba<0:
    ba=0

if lb!=0 or ra!=0:
    ans+=min(lb,ra)
    ans+=min(lb,ba)
    ans+=min(ra,ba)


print(ans)