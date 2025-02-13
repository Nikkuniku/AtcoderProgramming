from sortedcontainers import SortedList

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
S = SortedList(A)
ans = 0
for b in B:
    p = S.bisect_left(b)
    if p == len(S):
        ans = -1
        break
    ans += S[p]
    S.discard(S[p])
print(ans)
