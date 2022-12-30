n,m=map(int,input().split())

ids=[]

import bisect

arr=[[] for _ in range(n)]

for _ in range(m):
    p,y=map(int,input().split())
    ids.append([p,y])
    arr[p-1].append(y)

for i in range(n):
    arr[i]=sorted(arr[i])

for info in ids:
    p=info[0]
    y=info[1]
    index = bisect.bisect_left(arr[p-1],y)

    print(str(info[0]).zfill(6)+str(index+1).zfill(6))
