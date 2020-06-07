n,m = map(int,input().split())
a= list(map(lambda x: int(x)*(-1),input().split()))
b= list(map(lambda x: int(x)*(-1),input().split()))

import heapq
heapq.heapify(a)
heapq.heapify(b)

if n<m:
    print('NO')
    exit(0)

for i in range(m):
    yoyaku = heapq.heappop(b)*(-1)
    cap = heapq.heappop(a)*(-1)

    if yoyaku <= cap:
        continue
    else:
        print('NO')
        exit(0)

print('YES')