N=int(input())
Nums = list(map(int,input().split()))

import numpy as np
Nums.reverse()
cnt =0
d= np.array(Nums)

for i in range(N):
    P_i = d[0]
    d= np.delete(d,0)
    if (d>=P_i).prod() ==1:
        cnt +=1
    elif (d>=P_i).size ==0:
        cnt +=1

print(cnt)