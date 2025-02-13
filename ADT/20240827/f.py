from itertools import accumulate

N, Q = map(int, input().split())
S = input()
T = []
for i in range(N - 1):
    if S[i] == S[i + 1]:
        T.append(1)
    else:
        T.append(0)
cum = list(accumulate(T, initial=0))
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    r -= 1
    l -= 1
    ans.append(cum[r] - cum[l])
print(*ans, sep="\n")
