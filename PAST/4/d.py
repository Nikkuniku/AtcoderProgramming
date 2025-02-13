N = int(input())
S = list(input())


def f(s, t):
    res = S[:]
    for _ in range(s):
        tmp = ["."] * N
        for i in range(1, N):
            if res[i] == "#":
                tmp[i - 1] = "#"
                tmp[i] = "#"
        res = tmp[:]
    for _ in range(t):
        tmp = ["."] * N
        for i in range(N - 1):
            if res[i] == "#":
                tmp[i] = "#"
                tmp[i + 1] = "#"
        res = tmp[:]
    return res == ["#"] * N


ans = 1 << 60
p, q = -1, -1
for i in range(51):
    for j in range(51):
        if f(i, j):
            if ans > i + j:
                ans = min(ans, i + j)
                p = i
                q = j
print(p, q)
