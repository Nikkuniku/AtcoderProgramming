from itertools import accumulate

N, Q = map(int, input().split())
S = list(input())
C = [0]
for i in range(1, N):
    if S[i - 1] == S[i]:
        C.append(1)
    else:
        C.append(0)
cum = list(accumulate(C, initial=0))
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(cum[r] - cum[l])
print(*ans, sep="\n")
