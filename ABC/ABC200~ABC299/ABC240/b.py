n=int(input())
a=list(map(int,input().split()))

from collections import Counter
c=Counter(a)
ans=len(c.keys())
print(ans)