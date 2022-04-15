q=int(input())
import heapq
from collections import deque

normal_array=deque([])
sorted_array=[]

heapq.heapify(sorted_array)
ans=[]
for _ in range(q):
    c=list(map(int,input().split()))
    n=c[0]

    if n==1:
        normal_array.append(c[1])
    elif n==2:
        if sorted_array:
            v=heapq.heappop(sorted_array)
        else:
            v=normal_array.popleft()
        ans.append(v)
    else:
        while normal_array:
            v=normal_array.pop()
            heapq.heappush(sorted_array,v)
print(*ans,sep="\n")