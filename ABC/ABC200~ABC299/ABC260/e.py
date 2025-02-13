from itertools import accumulate

N, M = map(int, input().split())
Ids = [[] for _ in range(M + 1)]
for i in range(N):
    a, b = map(int, input().split())
    Ids[a].append(i)
    Ids[b].append(i)
ans = [0] * (M + 2)
cnt = [0] * N
K = 0
r = 0
for l in range(1, M + 1):
    while r + 1 < M + 1 and K < N:
        r += 1
        for i in Ids[r]:
            cnt[i] += 1
            if cnt[i] == 1:
                K += 1
    if K == N:
        ans[r - l + 1] += 1
        ans[M - l + 2] -= 1
    for i in Ids[l]:
        cnt[i] -= 1
        if cnt[i] == 0:
            K -= 1
cum_ans = list(accumulate(ans))
print(*cum_ans[1 : M + 1])
