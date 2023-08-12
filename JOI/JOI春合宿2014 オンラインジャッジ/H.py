from collections import defaultdict
N = int(input())
S = input()
INF = 1 << 60
d = defaultdict(lambda: -INF)
d[(0, 0, 0)] = -1
J, O, I = 0, 0, 0
dpJ, dpO, dpI = 0, 0, 0
ans = 0
for i in range(N):
    if S[i] == 'J':
        J += 1
        dpJ += 1
    elif S[i] == 'O':
        O += 1
        dpO += 1
    elif S[i] == 'I':
        I += 1
        dpI += 1
    m = min(J, O, I)
    J, O, I = J-m, O-m, I-m
    if (J, O, I) not in d:
        d[(J, O, I)] = i
    M = min(dpJ, dpO, dpI)
    if (dpJ-M, dpO-M, dpI-M) in d:
        ans = max(ans, i-d[(dpJ-M, dpO-M, dpI-M)])
print(ans)
