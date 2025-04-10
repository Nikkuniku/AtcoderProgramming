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


N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
powA = [[pow(A[i], r, MOD) for i in range(N)] for r in range(K + 1)]
cumA = [[0] * N for r in range(K + 1)]
for r in range(K + 1):
    cumA[r][-1] = powA[r][-1]
    for i in range(N - 1 - 1, -1, -1):
        temp = (powA[r][i] + cumA[r][i + 1]) % MOD
        cumA[r][i] = temp
print(cumA)
ans = []
res = 0
Binomial = BinomialCoefficient()
for r in range(1, K + 1):
    temp = 0
    for L in range(N):
        powA[r][L] * cumA[K]
