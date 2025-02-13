N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = 1 << 60
for s in range(1 << N):
    tmp = 0
    for i in range(N):
        if s & (1 << i):
            for j in range(M):
                if S[i][j] == "o":
                    tmp |= 1 << j
    if tmp == (1 << M) - 1:
        ans = min(ans, s.bit_count())
print(ans)
