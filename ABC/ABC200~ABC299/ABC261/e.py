n, c = map(int, input().split())
bit = [[[0, 1] for _ in range(30)] for _ in range(n+1)]
for i in range(n):
    t, a = map(int, input().split())
    if t == 1:
        for j in range(30):
            bit[i+1][j][0] = bit[i][j][0] & ((a & (1 << j)) >> j)
            bit[i+1][j][1] = bit[i][j][1] & ((a & (1 << j)) >> j)
    elif t == 2:
        for j in range(30):
            bit[i+1][j][0] = bit[i][j][0] | ((a & (1 << j)) >> j)
            bit[i+1][j][1] = bit[i][j][1] | ((a & (1 << j)) >> j)
    else:
        for j in range(30):
            bit[i+1][j][0] = bit[i][j][0] ^ ((a & (1 << j)) >> j)
            bit[i+1][j][1] = bit[i][j][1] ^ ((a & (1 << j)) >> j)

ans = []
tmp = c
for i in range(n):
    for j in range(30):
        x = tmp & (1 << j)
        if x:
            x = 1
        else:
            x = 0

        if bit[i+1][j][x] == 1:
            tmp |= (bit[i+1][j][x] << j)
        else:
            tmp &= ~(1 << j)
    ans.append(tmp)
print(*ans, sep="\n")
