from itertools import permutations
a = [9, 4, 6, 2]
ope = ['+', '-', '*', '/']
P = permutations(ope, 3)
for c in P:
    s = []
    for i in range(7):
        if i % 2 == 0:
            s.append(str(a[i//2]))
        else:
            s.append(c[i//2])
    tmp = ''.join(s)
    print(tmp)
