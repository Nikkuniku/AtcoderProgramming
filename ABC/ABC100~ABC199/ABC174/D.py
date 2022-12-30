n=int(input())
s=input()

from collections import Counter

c=Counter(s)

r=c['R']

cnt=0
for i in range(r):
    if s[i]=='W':
        cnt+=1


print(cnt)