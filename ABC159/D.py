import math
from collections import Counter

N=int(input())
Balls = list(map(int,input().split()))

def combinations_count(n, r):
    if n==1:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

for k in range(N):
    array_k = [Balls[i] for i in range(N) if i!=k]
    sum_k=0
    c= Counter(array_k)
    for j in list(c.values()):
        sum_k += combinations_count(j,2)
    
    print(sum_k)


