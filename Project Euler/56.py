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


L = 100
ans = 0
ka, kb = -1, -1
for a in range(1, L):
    A = list(map(int, list(str(a))))
    B = list(map(int, list(str(a))))
    for b in range(L):
        B = calc(A, B)
        tmp = sum(B)
        if ans < tmp:
            ans = max(ans, tmp)
            ka, kb = a, b
print(ans, ka, kb)
