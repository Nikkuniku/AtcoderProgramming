N=int(input())
A=list(map(int,input().split()))

import numpy as np

ones = np.ones(N)

total = np.sum(ones/A)

print(1/total)