N, M = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(M)]

res = []


def dfs(pattern, pos, i):
    if i == M:
        res.append(pattern)
        return
    a, b, c = C[i]
    a -= 1
    b -= 1
    if pos[a] != -1 and pos[b] != -1:
        if pos[a] - pos[b] == c:
            dfs(pattern, pos, i + 1)
    if pos[a] != -1:
        if 0 <= pos[a] - c and pattern[pos[a] - c] == -1 and pos[b] == -1:
            pattern[pos[a] - c] = b
            pos[b] = pos[a] - c
            dfs(pattern, pos, i + 1)
            pattern[pos[a] - c] = -1
            pos[b] = -1

    if pos[b] != -1:
        if pos[b] + c < N and pattern[pos[b] + c] == -1 and pos[a] == -1:
            pattern[pos[b] + c] = a
            pos[a] = pos[b] + c
            dfs(pattern, pos, i + 1)
            pattern[pos[b] + c] = -1
            pos[a] = -1
    for j in range(N):
        if not j + c < N:
            continue
        if pattern[j] == -1 and pattern[j + c] == -1:
            pattern[j + c] = a
            pattern[j] = b
            pos[a] = j + c
            pos[b] = j
            dfs(pattern, pos, i + 1)
            pattern[j + c] = -1
            pattern[j] = -1
            pos[a] = -1
            pos[b] = -1


P = [-1] * N
Q = [-1] * N
dfs(P, Q, 0)
