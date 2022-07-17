
from collections import Counter
from itertools import permutations
s1 = input()
s2 = input()
s3 = input()
c = Counter(s1)
c += Counter(s2)
c += Counter(s3)
n = len(c.keys())
g = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], n)
d = {}
for i, v in enumerate(c.keys()):
    d[v] = i
ans = 'UNSOLVABLE'

if n <= 10:
    for p in g:
        t1 = []
        t2 = []
        t3 = []
        if p[d[s1[0]]] == 0 or p[d[s2[0]]] == 0 or p[d[s3[0]]] == 0:
            continue
        for i in range(len(s1)):
            t1.append(str(p[d[s1[i]]]))
        for i in range(len(s2)):
            t2.append(str(p[d[s2[i]]]))
        for i in range(len(s3)):
            t3.append(str(p[d[s3[i]]]))
        t1 = int(''.join(t1))
        t2 = int(''.join(t2))
        t3 = int(''.join(t3))
        if t1+t2 == t3:
            print(t1)
            print(t2)
            print(t3)
            exit(0)

print(ans)
