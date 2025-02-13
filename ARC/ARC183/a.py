from sortedcontainers import SortedList

N, K = map(int, input().split())
S = SortedList()
for i in range(1, N + 1):
    for _ in range(K):
        S.add(i)
ans = []
if N % 2 == 0:
    ans.append(N // 2)
    S.discard(N // 2)
    while S:
        ans.append(S.pop())
else:
    for _ in range(K):
        S.discard((N + 1) // 2)
        ans.append((N + 1) // 2)
    p = ((N + 1) // 2) - 1
    if p in S:
        S.discard(((N + 1) // 2) - 1)
        ans.append(((N + 1) // 2) - 1)
    while S:
        ans.append(S.pop())
print(*ans)
