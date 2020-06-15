n=int(input())
a=list(map(int,input().split()))

ans='No'
from collections import Counter

c=Counter(a)
keys = list(c.keys())
values =list(c.values())

if keys==[0]:
    ans='Yes'
elif len(keys)==3 and values[0]==n/3 and values[1]==n/3 and keys[0]^keys[1]==keys[2]:
    ans='Yes'
elif len(keys)==2 and c[0]==n/3:
    ans='Yes'

print(ans)