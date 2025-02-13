import numpy as np

N = int(input())
A = list(map(int, input().split()))
mean = np.mean(A)
print(mean)
