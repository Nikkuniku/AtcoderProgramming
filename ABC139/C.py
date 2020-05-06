N=int(input())
Height =list(map(int,input().split()))

from itertools import groupby

ans = [ 1 if Height[i]>=Height[i+1] else 0 for i in range(N-1)  ]

gr = groupby(ans)

total=0
for key,value in gr:
    if key ==1:
        total=max(total,len(list(value)))

print(total)