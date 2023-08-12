from math import factorial
from collections import Counter
S = list(input())
C = Counter(S)
T = sorted(S)
ans = 0
for i in range(len(S)):
    for k, v in sorted(list(C.items())):
        if S[i] != k:
            cnt = -1
            div = 1
            for s, t in C.items():
                cnt += t
                if k == s:
                    div *= factorial(t-1)
                else:
                    div *= factorial(t)
            ans += factorial(cnt)//div
        else:
            break
    C[S[i]] -= 1
    if C[S[i]] == 0:
        C.pop(S[i])
print(ans+1)
