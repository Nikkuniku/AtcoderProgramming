N=int(input())
Takoyaki = list(map(int,input().split()))

from itertools import combinations

c = combinations(Takoyaki,2)

total=0

for i in c:
    total += i[0]*i[1]

print(total)