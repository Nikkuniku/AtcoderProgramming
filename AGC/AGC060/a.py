from string import ascii_lowercase
from collections import Counter
from math import ceil
N = int(input())
S = input()
dp = [26]*N
MOD = 998244353
# for L in range(3, N+1):
#     for i in range(N):
#         tmp = S[i:i+L]
#         if len(tmp) < L:
#             break
#         tmp = tmp.replace('?', '')
#         C = Counter(tmp)
#         if max(C.values()) >= ceil(L/2):
#             print(0)
#             print(tmp)
#             exit()

for i in range(N):
    if S[i] in ascii_lowercase:
        dp[i] = 1
        continue
    tmp = set()
    lquestion = 0
    for j in [-2, -1, 1, 2]:
        k = i+j
        if 0 <= i+j < N:
            if S[k] != '?':
                tmp.add(S[k])
        if 0 <= i+j < i:
            if S[k] == '?':
                lquestion += 1
    dp[i] -= len(tmp)
    dp[i] -= lquestion

ans = 1
for c in dp:
    ans *= c
    ans %= MOD
print(ans)
print(dp)
