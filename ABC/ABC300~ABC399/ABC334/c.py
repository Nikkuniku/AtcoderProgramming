from itertools import accumulate

N, K = map(int, input().split())
A = set(list(map(int, input().split())))
P = []
for i in range(1, N + 1):
    P.append(i)
    if i not in A:
        P.append(i)
diffs = []
ans = 1 << 60
if (2 * N - K) % 2 == 0:
    for i in range(len(P)):
        if i % 2 == 0:
            diffs.append(abs(P[i + 1] - P[i]))
    ans = sum(diffs)
else:
    for i in range(len(P)):
        if i % 2 == 0 and i + 1 <= len(P) - 1:
            diffs.append(abs(P[i + 1] - P[i]))
    diffs_odd = []
    for i in range(1, len(P)):
        if i % 2 == 1:
            diffs_odd.append(abs(P[i + 1] - P[i]))
    cum_even = list(accumulate(diffs, initial=0))
    cum_odd = list(accumulate(diffs_odd, initial=0))
    for i in range(len(P)):
        if i % 2 == 0:
            tmp = cum_odd[-1] - cum_odd[i // 2] + cum_even[i // 2]
        else:
            tmp = cum_odd[-1] - cum_odd[(i // 2) + 1]
            tmp += P[i + 1] - P[i - 1]
            tmp += cum_even[i // 2]
        ans = min(ans, tmp)
print(ans)
