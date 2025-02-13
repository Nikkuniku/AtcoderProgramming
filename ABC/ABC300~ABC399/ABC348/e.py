# 全方位木DP
import sys

input = sys.stdin.readline
from collections import deque

N = int(input())
X = [[] for i in range(N)]
for i in range(N - 1):
    x, y = map(int, input().split())
    X[x - 1].append(y - 1)
    X[y - 1].append(x - 1)
C = list(map(int, input().split()))
P = [-1] * N
Q = deque([0])
R = []
while Q:
    i = deque.popleft(Q)
    R.append(i)
    for a in X[i]:
        if a != P[i]:
            P[a] = i
            X[a].remove(i)
            deque.append(Q, a)

##### Settings
unit = 0
merge = lambda a, b: a + b
adj_bu = lambda a, i: a + 1
adj_td = lambda a, i, p: a + 1
adj_fin = lambda a, i: a
#####

ME = [unit] * N
XX = C
TD = [unit] * N
for i in R[1:][::-1]:
    XX[i] = adj_bu(ME[i], i)
    p = P[i]
    ME[p] = merge(ME[p], XX[i])
XX[R[0]] = adj_fin(ME[R[0]], R[0])

# print("ME =", ME) # Merge before adj
# print("XX =", XX) # Bottom-up after adj

for i in R:
    ac = TD[i]
    for j in X[i]:
        TD[j] = ac
        ac = merge(ac, XX[j])
    ac = unit
    for j in X[i][::-1]:
        TD[j] = adj_td(merge(TD[j], ac), j, i)
        ac = merge(ac, XX[j])
        XX[j] = adj_fin(merge(ME[j], TD[j]), j)

# print("TD =", TD) # Top-down after adj
# print("XX =", XX) # Final Result

print(*XX, sep="\n")
