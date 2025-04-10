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
        self.isprime[0] = self.isprime[1] = False
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


M = 10**6
ER = eratosthenes(M)
S = set()
Primes = []
for i in range(2, M + 1):
    if ER.isprime[i]:
        Primes.append(i)
for i in range(len(Primes)):
    for j in range(i + 1, len(Primes)):
        p = Primes[i]
        q = Primes[j]
        if p * q > M:
            break
        for k in range(1, 21):
            for m in range(1, 21):
                if pow(p, k) * pow(q, m) > M:
                    break
                S.add(pow(p, k) * pow(q, m))
L_Primes = sorted(S)
from bisect import bisect_right

Q = int(input())
ans = []
for _ in range(Q):
    A = int(input())e2
    key = bisect_right(L_Primes, int(A**0.5))
    ans.append(L_Primes[key - 1] ** 2)
print(*ans, sep="\n")
