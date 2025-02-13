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


N = int(input())
M = 2 * 10**6
# M = 10
ER = eratosthenes(M + 1)
ans = 0
for i in range(1, M + 1):
    if i**2 > N:
        break
    f = ER.factorize(i)
    res = 1
    for p, e in f:
        res *= 2 * e + 1
    if res == 9 and i**2 <= N:
        ans += 1
print(ans)
