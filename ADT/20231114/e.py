from string import ascii_lowercase
from collections import defaultdict

d = defaultdict(int)
X = input()
for i in range(26):
    d[X[i]] = ascii_lowercase[i]
N = int(input())
S = [input() for _ in range(N)]
T = []
for i in range(N):
    tmp = []
    for s in S[i]:
        tmp.append(d[s])
    T.append(("".join(tmp), S[i]))
T.sort()
for s, t in T:
    print(t)
