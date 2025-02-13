def rep(x, y, N, s):
    if s == 0:
        return x, y
    if s == 1:
        return y, N + 1 - x
    if s == 2:
        return N + 1 - x, N + 1 - y
    if s == 3:
        return N + 1 - y, x


N = int(input())
A = [list(input()) for _ in range(N)]
B = [list("." * N) for _ in range(N)]
s = 0
for i in range(N // 2):
    a, b = i + 1, i + 1
    c, d = N - i, N - i
    s = (s + 1) % 4
    for x in range(a, c + 1):
        p, q = rep(x, b, N, s)
        u, v = rep(x, d, N, s)
        B[p - 1][q - 1] = A[x - 1][b - 1]
        B[u - 1][v - 1] = A[x - 1][d - 1]
    for y in range(b, d + 1):
        p, q = rep(a, y, N, s)
        u, v = rep(c, y, N, s)
        B[p - 1][q - 1] = A[a - 1][y - 1]
        B[u - 1][v - 1] = A[c - 1][y - 1]
for c in B:
    print(*c, sep="")
