import math
from collections import Counter

N=int(input())
Balls = list(map(int,input().split()))

def combinations_count(n, r):
    if n==1:
        return 0
    else:
        return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
c = Counter(Balls)
d={}
ALL_SUM=0
for i,j in c.most_common():
    d[i]=j
    ALL_SUM+=combinations_count(j,2)
for k in Balls:
    print(ALL_SUM-(d[k] - 1))

# for k in range(N):
#     tmp=Balls[k]
#     array_k = Balls
#     sum_k=0
#     c= Counter(array_k)


#     for j in list(c.values()):
#         sum_k += combinations_count(j,2)
    
#     Balls.insert(k,tmp)
#     print(sum_k)
