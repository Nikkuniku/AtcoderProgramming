N=int(input())
IDs =list(map(int,input().split()))

from collections import Counter

c=Counter(IDs)

for i in range(1,N+1):
    print(c[i])