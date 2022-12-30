K = int(input())


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

# 素因数aがm個以上となる最小のN


def minimamu_n(a, m):
    l = 0
    r = K+1
    while r-l > 1:
        mid = (l+r)//2
        cnt = 0
        i = 1
        while True:
            cnt += mid//pow(a, i)
            i += 1
            if pow(a, i) > mid:
                break

        if cnt >= m:
            r = mid
        else:
            l = mid
    return r


primes = factorization(K)
ans = []
for p, c in primes:
    ans.append(minimamu_n(p, c))
print(max(ans))
