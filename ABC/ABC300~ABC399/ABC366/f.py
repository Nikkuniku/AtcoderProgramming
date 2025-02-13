from itertools import permutations

N, K = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[1], reverse=True)
AB.sort(key=lambda x: x[0], reverse=True)
if len(AB) > 10:
    AB = AB[:K]
P = list(permutations(range(len(AB))))
ans = 0
for c in P:
    x = 1
    for i in range(min(len(AB), K)):
        a, b = AB[c[i]]
        x = a * x + b
    ans = max(ans, x)
print(ans)
