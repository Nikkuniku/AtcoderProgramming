"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
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


n = int(input())
ans = 0
for i in range(1, n+1):
    arr = factorization(i)
    k = 1
    for r in arr:
        if r[1] % 2 == 0:
            continue
        else:
            k *= r[0]

    for c in range(1, n+1):
        if k*(c**2) <= n:
            ans += 1
        else:
            break
print(ans)
