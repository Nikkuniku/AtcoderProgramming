N,K,Q = map(int,input().split())

import numpy as np

points=np.array([K]*N)
dis = np.array([0]*N)
for i in range(Q):
    a = int(input())
    a=a-1
    dis[a]+=1

points-=Q
points += dis

for j in points:
    if j>0:
        print('Yes')
    else:
        print('No')