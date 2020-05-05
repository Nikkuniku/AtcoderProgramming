N,K = map(int,input().split())

import numpy as np

H=list(map(int,input().split()))
Hs = np.array(H)

print(np.sum(np.where(Hs>=K,1,0)))