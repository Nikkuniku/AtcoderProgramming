N = int(input())
C = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]
for x in range(N):
    for y in range(N):
        A = list(map(int, input().split()))
        for z in range(N):
            C[z + 1][x + 1][y + 1] = A[z]
ans = []
for z in range(N + 1):
    for x in range(N + 1):
        for y in range(N):
            C[z][x][y + 1] += C[z][x][y]
for z in range(N + 1):
    for y in range(N + 1):
        for x in range(N):
            C[z][x + 1][y] += C[z][x][y]
for z in range(N):
    for x in range(N + 1):
        for y in range(N + 1):
            C[z + 1][x][y] += C[z][x][y]

Q = int(input())
for _ in range(Q):
    lx, rx, ly, ry, lz, rz = map(int, input().split())
    tmp = (
        C[rz][rx][ry]
        - C[rz][lx - 1][ry]
        - C[rz][rx][ly - 1]
        + C[rz][lx - 1][ly - 1]
        - C[lz - 1][rx][ry]
        + C[lz - 1][lx - 1][ry]
        + C[lz - 1][rx][ly - 1]
        - C[lz - 1][lx - 1][ly - 1]
    )

    ans.append(tmp)
print(*ans, sep="\n")
