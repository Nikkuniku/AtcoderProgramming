class BinomialCoefficient:
    def __init__(self) -> None:
        self.MOD = 998244353
        self.N = 5 * 10**6  # N は必要分だけ用意する
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


binomial = BinomialCoefficient()
A, B, C, D = map(int, input().split())
ans = 0
for i in range(C + 1):
    temp = binomial.cmb(A + B + i, B) * binomial.cmb(C - i + D - 1, D - 1)
    temp %= binomial.MOD
    ans += temp
    ans %= binomial.MOD
print(ans)
