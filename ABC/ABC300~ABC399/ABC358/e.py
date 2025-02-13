class BinomialCoefficient:
    def __init__(self) -> None:
        self.MOD = 998244353
        self.N = 2 * 10**5  # N は必要分だけ用意する
        self.fact = [1, 1]  # fact[n] = (n! mod p)
        self.factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
        self.inv = [0, 1]  # factinv 計算用

        for i in range(2, self.N + 1):
            self.fact.append((self.fact[-1] * i) % self.MOD)
            self.inv.append((-self.inv[self.MOD % i] * (self.MOD // i)) % self.MOD)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % self.MOD)

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
K = int(input())
C = list(map(int, input().split()))
M = len(C)
dp = [[0] * (K + 1) for _ in range(M + 1)]
dp[0][0] = 1
MOD = 998244353
for i in range(M):
    for j in range(K + 1):
        for k in range(min(j, C[i]) + 1):
            dp[i + 1][j] += dp[i][j - k] * binomial.cmb(j, k)
            dp[i + 1][j] %= MOD
ans = (sum(dp[M]) - 1) % MOD
print(ans)
