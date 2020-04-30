N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))

from itertools import permutations
from math import factorial

X=[i+1 for i in range(N)]
X_list = list(permutations(X))

P=tuple(P)
Q=tuple(Q)

ans=[0,0]
for j in range(factorial(N)):
    if X_list[j]==P:
        ans[0] = j
        break
for k in range(factorial(N)):
    if X_list[k]==Q:
        ans[1] = k
        break
print(abs(ans[0]-ans[1]))
