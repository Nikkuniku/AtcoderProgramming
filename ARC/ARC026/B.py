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


N = int(input())
primes = factorization(N)
if N == 1:
    print('Deficient')
    exit()
res = 1
for p, e in primes:
    res *= (pow(p, e+1)-1)//(p-1)
res -= N
ans = 'Perfect'
if N < res:
    ans = 'Abundant'
elif N > res:
    ans = 'Deficient'
print(ans)
