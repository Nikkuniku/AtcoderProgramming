import math
from random import random, randint
from collections import defaultdict
n, b1, b2, b3 = map(int, input().split())
L = []
R = []
for _ in range(n):
    L.append(list(map(int, input().split())))
for _ in range(n):
    R.append(list(map(int, input().split())))
grid = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        grid[i][j] = randint(L[i][j], R[i][j])


def score():
    re = 0
    cumrow = [[0] for _ in range(n)]
    cumcol = [[0] for _ in range(n)]
    d = defaultdict(int)
    for i in range(n):
        for j in range(n):
            cumrow[i].append(cumrow[i][-1]+grid[i][j])
            cumcol[i].append(cumcol[i][-1]+grid[j][i])
    for i in range(n):
        for j in range(n):
            for k in range(j+1, n+1):
                a = cumrow[i][k]-cumrow[i][j]
                b = cumcol[i][k]-cumcol[i][j]
                if k-j == 1:
                    d[a] += 1
                else:
                    d[a] += 1
                    d[b] += 1
    re = b1*d[b1] + b2*d[b2]+b3*d[b3]
    return re


def aneealfunction(de, Temp):
    p = math.exp(-abs(de)/Temp)
    return p


T = 1000
cool = 0.95
old_score = 0
new_score = 0
while T > 0.001:
    old_score = score()

    ij = randint(0, (n**2)-1)
    g_i = ij//n
    g_j = ij % n
    tmp = randint(L[g_i][g_j], R[g_i][g_j])
    grid[g_i][g_j], tmp = tmp, grid[g_i][g_j]
    new_score = score()

    p = aneealfunction(new_score-old_score, T)
    if new_score > old_score or random() < p:
        T *= cool
        continue
    else:
        grid[g_i][g_j], tmp = tmp, grid[g_i][g_j]
        T *= cool

for i in range(n):
    print(*grid[i])
