N=int(input())

import math
from itertools import permutations

town=[i+1 for i in range(N)]

roots = list(permutations(town))

# print(*roots,sep="\n")

info = []

for i in range(N):
    x,y=map(int,input().split())
    info.append([x,y])

total = 0 

for road in roots:
    for j in range(len(road)):
        if j==0:
            continue
        to = road[j]
        fr = road[j-1]

        total += math.sqrt( (info[to-1][0]-info[fr-1][0])**2 + (info[to-1][1] - info[fr-1][1])**2 )

print(total/math.factorial(N))
