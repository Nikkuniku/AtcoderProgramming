N=int(input())

seq=[]

for i in range(N):
    a= int(input())
    seq.append(a)

import heapq

tmp=list(map(lambda x: x*(-1),seq))
heapq.heapify(tmp)

a=heapq.heappop(tmp)*(-1)
b=heapq.heappop(tmp)*(-1)

for j in range(N):
    if seq[j]==a:
        print(b)
    else:
        print(a)
