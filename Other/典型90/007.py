n=int(input())
a=list(map(int,input().split()))
q=int(input())

a=sorted(a)

import bisect

arr=[]
for _ in range(q):
    b=int(input())

    i = bisect.bisect_left(a,b)

    ans = float('inf')
    for j in [-1,0,1]:
        if 0<=i+j<=n-1:
            ans =min(ans,abs(a[i+j]-b))

    arr.append(ans)

for k in range(q):
    print(arr[k])

