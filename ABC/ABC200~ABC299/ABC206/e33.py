class eratosthenes:
    def __init__(self, N: int) -> None:
        """
        Nまでの素数を列挙
        Parameters
        ----------
        N:int
        """
        self.N = N
        self.isprime = [True] * (N + 1)
        self.minfactor = [-1] * (N + 1)
        self.isprime[1] = False
        self.minfactor[1] = 1
        self.mobius = [1] * (N + 1)
        self.primecnt = 0
        # ふるう
        for p in range(2, self.N + 1):
            if not self.isprime[p]:
                continue
            self.minfactor[p] = p
            self.mobius[p] = -1
            self.primecnt += 1
            for q in range(2 * p, N + 1, p):
                self.isprime[q] = False
                if self.minfactor[q] == -1:
                    self.minfactor[q] = p
                if (q // p) % p == 0:
                    self.mobius[q] = 0
                else:
                    self.mobius[q] = -self.mobius[q]

    def factorize(self, n: int) -> list:
        """
        nの素因数分解
        O(logn)
        Parameters
        ----------
        n:int
        """
        res = []
        while n > 1:
            p = self.minfactor[n]
            exp = 0
            while self.minfactor[n] == p:
                n //= p
                exp += 1
            res.append((p, exp))
        return res

    def divisors(self, n: int) -> list:
        """
        nの約数列挙
        O(sigma(n))~O(n^(1/3))
        Parameters
        ----------
        n:int
        """
        res = [1]
        factor = self.factorize(n)
        for p, e in factor:
            M = len(res)
            for i in range(M):
                v = 1
                for _ in range(e):
                    v *= p
                    res.append(res[i] * v)
        return res


from math import comb

L, R = map(int, input().split())
ER = eratosthenes(R + 1)
soinsuu = [True] * (R + 1)
soinsuu_odd = [False] * (R + 1)
for k in range(2, R + 1):
    primes = ER.factorize(k)
    if len(primes) % 2 != 0:
        soinsuu_odd[k] = True
    for _, e in primes:
        if e >= 2:
            soinsuu[k] = False
            break
ans = 0
for k in range(2, R + 1):
    if not soinsuu[k]:
        continue
    A = R // k - ((L - 1) // k)
    if soinsuu_odd[k]:
        ans += A * (A - 1) // 2
    else:
        ans -= A * (A - 1) // 2
for k in range(max(2, L), R + 1):
    ans -= R // k - 1
ans *= 2
print(ans)
