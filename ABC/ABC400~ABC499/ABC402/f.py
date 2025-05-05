N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dij = [(1, 0), (0, 1)]


def paths(si, sj, N, A, dij):
    from collections import defaultdict

    D = defaultdict(list)
    for s in range(1 << N):
        ni, nj = si, sj
        val = A[ni][nj]
        for t in range(N):
            if s & (1 << t):
                ni += dij[0][0]
                nj += dij[0][1]
            else:
                ni += dij[1][0]
                nj += dij[1][1]
            val = (10 * val + A[ni][nj]) % M
        D[s.bit_count()].append(val)
    return D


def paths2(si, sj, N, A, dij):
    from collections import defaultdict

    D = defaultdict(list)
    for s in range(1 << N):
        ni, nj = si, sj
        val = A[ni][nj]
        for t in range(N):
            if s & (1 << t):
                ni -= dij[0][0]
                nj -= dij[0][1]
            else:
                ni -= dij[1][0]
                nj -= dij[1][1]
            val = (val + A[ni][nj] * pow(10, t + 1, M)) % M
        D[s.bit_count()].append(val)
    return D


S = paths(0, 0, (N + 1) // 2, A, dij)
T = paths2(N - 1, N - 1, (N + 1) // 2, A, dij)
print(S)
ans = 0
for i in range(N):
    for m in S[i]:
        k = A[i][N - 1 - i]
        for p in T[N - 1 - i]:
            temp = m * pow(10, N - 1, M) + p - k * pow(10, N - 1, M)
            temp %= M
            ans = max(ans, temp)
print(ans)
