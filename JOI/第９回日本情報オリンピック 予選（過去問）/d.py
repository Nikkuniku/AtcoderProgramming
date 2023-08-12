from itertools import permutations
N = int(input())
K = int(input())
S = set()
Card = [input() for _ in range(N)]
P = list(permutations(Card, K))
for c in P:
    tmp = ''.join(c)
    S.add(tmp)
print(len(S))
