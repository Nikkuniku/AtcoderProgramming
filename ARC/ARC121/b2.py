from itertools import permutations
from random import randint


def gen(n, s):
    re = []
    for _ in range(n):
        re.append((randint(1, 1000), s))
    return re


arr = gen(6, 'R')+gen(3, 'G')+gen(1, 'B')
print(arr)

p = permutations(arr)

ans = 10**18
r = []
for c in p:
    tmp = 0
    for i in range(5):
        if c[2*i][1] == c[2*i+1][1]:
            pass
        else:
            tmp += abs(c[2*i][0]-c[2*i+1][0])

    if tmp < ans:
        ans = tmp
        r = c

print(ans)
print(r)
print(sorted(arr, key=lambda x: x[0]))
print(5)
for p in arr:
    print(*list(p))
