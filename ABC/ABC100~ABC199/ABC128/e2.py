from sortedcontainers import SortedSet

N, Q = map(int, input().split())
E = []
for _ in range(N):
    s, t, x = map(int, input().split())
    E.append((s - x, 1, x))
    E.append((t - x, -1, x))
E.sort()
ans = []
D = [int(input()) for _ in range(Q)]
k = 0
S = SortedSet()
for q in range(Q):
    while k < len(E) and E[k][0] <= D[q]:
        type = E[k][1]
        if type == 1:
            S.add(E[k][2])
        else:
            S.discard(E[k][2])
        k += 1
    if S:
        ans.append(S[0])
    else:
        ans.append(-1)
print(*ans, sep="\n")
