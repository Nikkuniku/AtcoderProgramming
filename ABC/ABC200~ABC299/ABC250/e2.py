from collections import defaultdict
from random import sample
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
hash_A, hash_B = [0], [0]
setA, setB = set(), set()
d = defaultdict(int)
randomval = sample(range(10**7), k=len(set(A+B)))
for i, v in enumerate(list(set(A+B))):
    d[v] = randomval[i]

for i in range(N):
    if A[i] in setA:
        hash_A.append(hash_A[-1])
    else:
        hash_A.append(hash_A[-1] ^ d[A[i]])
        setA.add(A[i])
    if B[i] in setB:
        hash_B.append(hash_B[-1])
    else:
        hash_B.append(hash_B[-1] ^ d[B[i]])
        setB.add(B[i])

ans = []
Q = int(input())
for _ in range(Q):
    x, y = map(int, input().split())
    res = 'No'
    if hash_A[x] == hash_B[y]:
        res = 'Yes'
    ans.append(res)
print(*ans, sep="\n")
