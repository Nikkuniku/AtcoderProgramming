N, K = map(int, input().split())
Black = [[0] * (2 * K + 1) for _ in range(2 * K + 1)]
White = [[0] * (2 * K + 1) for _ in range(2 * K + 1)]
for _ in range(N):
    x, y, c = input().split()
    x = int(x) % (2 * K) + 1
    y = int(y) % (2 * K) + 1
    if c == "B":
        Black[x][y] += 1
    elif c == "W":
        White[x][y] += 1
for i in range(2 * K + 1):
    for j in range(2 * K):
        Black[i][j + 1] += Black[i][j]
        White[i][j + 1] += White[i][j]
for j in range(2 * K + 1):
    for i in range(2 * K):
        Black[i + 1][j] += Black[i][j]
        White[i + 1][j] += White[i][j]
ans = 0
for i in range(2 * K):
    for j in range(2 * K):
        if i + 1 + K <= 2 * K and j + 1 + K <= 2 * K:
            b = (
                Black[i + 1 + K][j + 1 + K]
                - Black[i][j + 1 + K]
                - Black[i + 1 + K][j]
                + Black[i][j]
            )
            w = White[2 * K][2 * K] - (
                White[i + 1 + K][j + 1 + K]
                - White[i][j + 1 + K]
                - White[i + 1 + K][j]
                + White[i][j]
            )
        elif i + 1 + K <= 2 * K and j + 1 + K > 2 * K:
            b = (
                Black[i + 1 + K][2 * K]
                - Black[i][2 * K]
                - Black[i + 1 + K][j]
                + Black[i][j]
                + Black[i + 1 + K][(j + 1 + K) % (2 * K) + 1]
                - Black[i][(j + 1 + K) % (2 * K) + 1]
            )
            w = (
                White[i + 1 + K][2 * K]
                - White[i][2 * K]
                - White[i + 1 + K][j]
                + White[i][j]
                + White[i + 1 + K][(j + 1 + K) % (2 * K) + 1]
                - White[i][(j + 1 + K) % (2 * K) + 1]
            )
        elif i + 1 + K > 2 * K and j + 1 + K <= 2 * K:
            b = (
                Black[2 * K][j + 1 + K]
                - Black[2 * K][j]
                - Black[i][j + 1 + K]
                + Black[i][j]
                + Black[(i + 1 + K) % (2 * K) + 1][j + 1 + K]
                - Black[(i + 1 + K) % (2 * K) + 1][j]
            )
            w = (
                White[2 * K][j + 1 + K]
                - White[2 * K][j]
                - White[i][j + 1 + K]
                + White[i][j]
                + White[(i + 1 + K) % (2 * K) + 1][j + 1 + K]
                - White[(i + 1 + K) % (2 * K) + 1][j]
            )
        else:
            b = (
                Black[2 * K][2 * K]
                - Black[i][2 * K]
                - Black[2 * K][j]
                + Black[i][j]
                + Black[(i + 1 + K) % (2 * K) + 1][(j + 1 + K) % (2 * K) + 1]
            )
            w = (
                White[2 * K][2 * K]
                - White[i][2 * K]
                - White[2 * K][j]
                + White[i][j]
                + White[(i + 1 + K) % (2 * K) + 1][(j + 1 + K) % (2 * K) + 1]
            )
        ans = max(ans, b + w)
print(ans)
