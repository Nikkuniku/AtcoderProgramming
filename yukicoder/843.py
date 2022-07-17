n = int(input())


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


primes = Eratosthenes(n)
list_prime = []
for i in range(len(primes)):
    if primes[i]:
        list_prime.append(i)

set_prime = set(list_prime)

p = 2
ans = 0
for r in list_prime:
    q = r**2 - p
    if q in set_prime:
        ans += 1
        if p != q:
            ans += 1
print(ans)
