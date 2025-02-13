def calc(a, b):
    a = a[::-1]
    b = b[::-1]
    res = [0] * (len(a) + len(b))
    if len(a) < len(b):
        a, b = b, a
    for i in range(len(b)):
        for j in range(len(a)):
            k = b[i] * a[j]
            res[i + j] += k % 10
            res[i + j + 1] += k // 10
    for i in range(len(res) - 1):
        res[i + 1] += res[i] // 10
        res[i] %= 10
    res = res[::-1]
    return res


S = [1]
N = 100
for v in range(2, N + 1):
    T = list(map(int, list(str(v))))
    S = calc(S, T)
print(S)
print(sum(S))
