import numpy as np
N = int(input())
AB = np.array([list(map(int, input().split())) for _ in range(N)])
med_a = np.median(AB[:, 0])
med_b = np.median(AB[:, 1])
ans = med_b-med_a+1
if N % 2 == 0:
    ans = 2*(med_b-med_a)+1
ans = int(ans)
print(ans)
