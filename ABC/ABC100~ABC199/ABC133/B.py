N,D = map(int,input().split())

from itertools import combinations
from fractions import math

points=[]
for i in range(N):
    points.append([list(map(int,input().split()))])

c = list(combinations(points,2))

cnt = 0

for combi in c:
    distance = 0

    for j in range(D):
        X=combi[0][0]
        Y=combi[1][0]
        distance += ( X[j] - Y[j])**2

    distance = math.sqrt(distance)

    if distance.is_integer():
        cnt+=1

print(cnt)