"""nを素因数分解"""

"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


N = int(input())
ans = 0
for i in range(1, N + 1):
    factors_i = factorization(i)
    t = 1
    for p, e in factors_i:
        t *= p if e % 2 != 0 else 1
    l = 1
    r = N + 1
    while r - l > 1:
        mid = (l + r) // 2
        if t * mid * mid <= N:
            l = mid
        else:
            r = mid
    ans += l
print(ans)
