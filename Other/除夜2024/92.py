N, M = map(int, input().split())
S = [input() for _ in range(N)]
ans = 1 << 60
for i in range(1 << N):
    res = 0
    cnt = [0] * M
    for j in range(N):
        if i & (1 << j):
            res += 1
            for k in range(M):
                if S[j][k] == "o":
                    cnt[k] += 1
    if min(cnt) > 0:
        ans = min(ans, res)
print(ans)
