from collections import defaultdict
from random import randint

R = randint(1, 1 << 60)
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(list)
for i, v in enumerate(A):
    d[v ^ R].append(i)
ans = []
for i in range(N - 1, -1, -1):
    v = A[i] ^ R
    d[v].pop()
    if d[v]:
        ans.append(d[v][-1] + 1)
    else:
        ans.append(-1)
print(*ans[::-1])
