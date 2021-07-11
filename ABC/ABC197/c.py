n=int(input())
a=list(map(int,input().split()))

from collections import deque
    
ans = 10**9 +7
for i in range(1,2**(n-1)):
    tmp_min=0
    pre=0
    tmp=a[n-1]
    for j in range(n-1):
        if ((i>>j)&pre):
            tmp|=a[n-1-j-1]
            t= i>>j
            pre = i>>j
        else:
            tmp_min^=tmp
            tmp=a[n-1-j-1]
            t= i>>j
            pre = i>>j
    tmp_min^=tmp

    ans= min(tmp_min,ans)

print(2>>0)
print(ans)