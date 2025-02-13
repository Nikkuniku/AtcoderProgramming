N = int(input())

ans = [["."] * pow(3, N) for _ in range(pow(3, N))]


def f(k, i, j):
    if k == 0:
        ans[i][j] = "#"
        return
    step = int(pow(3, k - 1))
    for si in range(0, pow(3, k), step):
        for sj in range(0, pow(3, k), step):
            if si == sj == pow(3, k - 1):
                continue
            f(k - 1, i + si, j + sj)


f(N, 0, 0)
for c in ans:
    print(*c, sep="")
