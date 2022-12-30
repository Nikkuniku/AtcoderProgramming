n=int(input())
a=list(map(int,input().split()))

ans=a.copy()


#-1したもの
for i in range(n):
    if a[i]>=1:
        ans.append(a[i]-1)

for j in range(n):
    if a[j]<10**5:
        ans.append(a[j]+1)

from collections import Counter

c=Counter(ans)

v=max(c.values())

print(v)