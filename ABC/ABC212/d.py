import heapq

Q=int(input())
s=[]
heapq.heapify(s)

margin=0
for _ in range(Q):
    query=list(map(int,input().split()))
    p=query[0]
    if p==1:
        x=query[1]-margin
        heapq.heappush(s,x)
    elif p==2:
        x=query[1]
        margin+=x
    else:
        v=heapq.heappop(s)+margin
        print(v)