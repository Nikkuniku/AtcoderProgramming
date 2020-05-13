n=int(input())
h = list(map(int,input().split()))

import numpy as np

h = np.array(h)

cnt =1
for i in range(1,n):
    
    flg=0
    for j in range(i):

        if h[j]>h[i]:
            flg+=1

    if flg==0:
        cnt+=1


print(cnt)        

