n=int(input())
a=list(map(int,input().split()))

from collections import Counter

c=Counter(a)

v=list(c.values())
k=list(c.keys())

v=sorted(v)
k=sorted(k)

ans='Yes'
if len(k)==3:
    for i in range(3):
        if v[i]!=n/3:
            ans='No'
            break
elif len(k)==2:
    for j in range(2):
        if j==0:
            if not(k[j]==0 and v[j]==n/3):
                ans='No'
        elif j==1:
            if v[j]!=2*n/3:
                ans='No'
elif len(k)==1 and k[0]==0:
    ans='Yes'
else:
    ans='No'

print(ans)