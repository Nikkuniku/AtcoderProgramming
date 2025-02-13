N, Q = map(int, input().split())
black = [[0] * (N + 1) for _ in range(N + 1)]
P = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if P[i][j] == "B":
            black[i + 1][j + 1] += 1
for i in range(N):
    for j in range(N + 1):
        black[i + 1][j] += black[i][j]
for j in range(N):
    for i in range(N + 1):
        black[i][j + 1] += black[i][j]
ans = []


def g(x, y):
    res = black[(x % N) + 1][(y % N) + 1]
    col = y // N
    row = x // N
    res += black[-1][(y % N) + 1] * row
    res += black[(x % N) + 1][-1] * col
    res += black[-1][-1] * row * col
    return res


for _ in range(Q):
    A, B, C, D = map(int, input().split())
    tmp = g(C, D) + g(A - 1, B - 1) - g(A - 1, D) - g(C, B - 1)
    ans.append(tmp)
print(*ans, sep="\n")
