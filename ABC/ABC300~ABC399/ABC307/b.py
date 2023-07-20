from itertools import permutations
N = int(input())
S = [input() for _ in range(N)]
P = list(permutations(S, 2))
ans = 'No'
for c in P:
    tmp = [c[0], c[1]]
    tmps = ''.join(tmp)
    rev = tmps[::-1]
    if tmps == rev:
        ans = 'Yes'
print(ans)
