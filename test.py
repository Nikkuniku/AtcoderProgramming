from itertools import permutations
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import run_length, pairwise

a = [9, 4, 6, 2]
ope = ["+", "-", "*", "/"]
P = permutations(ope, 3)
for c in P:
    s = []
    for i in range(7):
        if i % 2 == 0:
            s.append(str(a[i // 2]))
        else:
            s.append(c[i // 2])
    tmp = "".join(s)
    print(tmp)

tmp = []
tmp.sort()
print(tmp)

A = [1, 1, 1, 2, 3, 3, 5, 6, 4, 5, 67, 82, 2, 2, 2, 1]
print(list(run_length.encode(A)))
B = [1, 2, 3, 4, 5]
C = list(pairwise(B))
print(C)
