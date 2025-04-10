from itertools import accumulate


class BinomialCoefficient:
    def __init__(self) -> None:
        self.MOD = 998244353
        self.N = 2 * 10**5  # N は必要分だけ用意する
        self.fact = [1] * (self.N + 1)  # fact[n] = (n! mod p)
        self.factinv = [1] * (self.N + 1)  # factinv[n] = ((n!)^(-1) mod p)

        for i in range(1, self.N):
            self.fact[i + 1] = (self.fact[i] * (i + 1)) % self.MOD
        self.factinv[self.N] = pow(self.fact[self.N], self.MOD - 2, self.MOD)
        for i in range(self.N, 0, -1):
            self.factinv[i - 1] = (self.factinv[i] * i) % self.MOD

    def cmb(self, n: int, r: int):
        """
        2項係数nCrを返す
        Parameters
        ----------
        n:int
        r:int
        """
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % self.MOD

    def Hom(self, n: int, r: int):
        """
        重複組み合わせnHrを返す
        Parameters
        ----------
        n:int
        r:int
        """
        return self.cmb(n + r - 1, r)


Binomial = BinomialCoefficient()
N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
cum = list(accumulate(A, initial=0))
Slp = [[0] for _ in range(K + 1)]
for p in range(K + 1):
    for r in range(N + 1):
        temp = (Slp[p][-1] + pow(-cum[r], K - p, MOD)) % MOD
        Slp[p].append(temp)
ans = 0
for r in range(N):
    for p in range(K + 1):
        temp = (Binomial.cmb(K, p) * pow(cum[r + 1], p, MOD) * Slp[p][r + 1]) % MOD
        ans += temp
        ans %= MOD
print(ans)
