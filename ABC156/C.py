import numpy as np
import math


N=int(input())
X_s = list(map(int,input().split()))

X_s = np.array(X_s)
P=np.sum(X_s)/N

P_floor = math.floor(P)
P_ceil = math.ceil(P)

A=np.sum((X_s-P_floor)**2)
B=np.sum((X_s-P_ceil)**2)

print(min(A,B))