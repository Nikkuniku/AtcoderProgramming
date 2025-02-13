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


N = 1548136
L = 5000
ER = eratosthenes(N + 1)
Primes = []
for p in range(2, N):
    if p >= L:
        break
    if ER.isprime[p]:
        Primes.append(p)
M = sum(Primes)
MOD = pow(10, 16)
dp = [[0] * (M + 1) for _ in range(len(Primes) + 1)]
dp[0][0] = 1
for i, p in enumerate(Primes):
    for m in range(M + 1):
        dp[i + 1][m] = dp[i][m]
        if m - p >= 0:
            dp[i + 1][m] += dp[i][m - p]
        dp[i + 1][m] %= MOD
ans = 0
for m in range(M + 1):
    if ER.isprime[m]:
        ans += dp[len(Primes)][m]
        ans %= MOD
print(ans)
