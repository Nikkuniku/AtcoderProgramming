# 1 以上 N 以下の整数が素数かどうかを返す
import bisect


def Eratosthenes(N):
    # テーブル
    isprime = [True] * (N+1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか
    return isprime


# エラトステネスの篩
isprime = Eratosthenes(pow(10, 6)+1)
primes = []
for i in range(len(isprime)):
    if isprime[i]:
        primes.append(i)
n = int(input())
idx = bisect.bisect_right(primes, n**(1/3))
ans = 0
for i in range(idx-1, -1, -1):
    q = primes[i]
    n_q = n/(q**3)
    p = bisect.bisect_right(primes, n_q)
    if p >= i:
        ans += i
    else:
        ans += p
print(ans)
