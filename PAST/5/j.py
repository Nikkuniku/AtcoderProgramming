from string import ascii_lowercase
from bisect import bisect_left

S = input()
X = int(input())
p = [""]
v = [0]
alp = set(list(ascii_lowercase))
for i, s in enumerate(S):
    if s in alp:
        p.append(s)
        v.append(v[-1] + 1)
    else:
        p.append(int(s))
        v.append(v[-1] * (int(s) + 1))
    if v[-1] >= X:
        break
while 1:
    idx = bisect_left(v, X)
    if v[idx] == X:
        if p[idx] in alp:
            exit(print(p[idx]))
        else:
            if p[idx - 1] in alp:
                exit(print(p[idx - 1]))
            else:
                X -= v[idx - 1] * p[idx]
    else:
        k = (X - 1) // v[idx - 1]
        X -= v[idx - 1] * k
