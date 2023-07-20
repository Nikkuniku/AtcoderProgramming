from collections import defaultdict
N = int(input())
d = defaultdict(int)
S = set()
C = []
D = []
for i in range(N):
    a, b = map(int, input().split())
    S.add(a)
    S.add(b)
    C.append([a, i+1, 'omote'])
    C.append([b, i+1, 'ura'])
S = sorted(list(S))
for i in range(len(S)):
    d[S[i]] = i+1
C.sort()
D = C[::]
print(*D)
for i in range(len(C)):
    C[i][0] = d[C[i][0]]
print(*C)
print(701849287+619875818+610749017+552987438+518975015)
