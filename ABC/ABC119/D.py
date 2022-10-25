from bisect import bisect_left
a, b, q = map(int, input().split())
S = [int(input()) for _ in range(a)]
T = [int(input()) for _ in range(b)]
INF = 1000_000_000_000_000
ans = []
for _ in range(q):
    tmp = INF
    s1, t1, s2, t2 = -1, -1, -1, -1
    x = int(input())
    idx_s = bisect_left(S, x)
    idx_t = bisect_left(T, x)
    if idx_s-1 >= 0:
        s1 = S[idx_s-1]
    if idx_s <= a-1:
        s2 = S[idx_s]
    if idx_t-1 >= 0:
        t1 = T[idx_t-1]
    if idx_t <= b-1:
        t2 = T[idx_t]

    if s1 != -1 and t2 != -1:
        tmp = min(tmp, min(abs(t2-x), abs(x-s1))+abs(t2-s1))
    if s2 != -1 and t1 != -1:
        tmp = min(tmp, min(abs(t1-x), abs(s2-x))+abs(s2-t1))
    if s1 != -1 and t1 != -1:
        tmp = min(tmp, abs(min(s1, t1)-x))
    if s2 != -1 and t2 != -1:
        tmp = min(tmp, abs(max(s2, t2)-x))

    ans.append(tmp)

print(*ans, sep="\n")
