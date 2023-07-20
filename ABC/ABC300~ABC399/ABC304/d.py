from bisect import bisect_right
from collections import defaultdict
W, H = map(int, input().split())
N = int(input())
Cakes = [list(map(int, input().split())) for _ in range(N)]
A = int(input())
X = list(map(int, input().split()))
cuts = [[] for _ in range(A+1)]
B = int(input())
Y = list(map(int, input().split()))
for i in range(N):
    a, b = Cakes[i]
    idx = bisect_right(X, a)
    cuts[idx].append(b)
d = defaultdict(int)
for i in range(A+1):
    for j in range(len(cuts[i])):
        idx = bisect_right(Y, cuts[i][j])
        d[(i, idx)] += 1
ans_min = 0
if len(list(d.keys())) == (A+1)*(B+1):
    ans_min = min(d.values())
ans_max = max(d.values())
print(ans_min, ans_max)
