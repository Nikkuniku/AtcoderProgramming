class BinomialCoefficient:
    def __init__(self) -> None:
        self.MOD = 1000000007
        self.N = 2 * 10**5  # N は必要分だけ用意する
        self.fact = [1, 1]  # fact[n] = (n! mod p)
        self.factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
        self.inv = [0, 1]  # factinv 計算用

        for i in range(2, self.N + 1):
            self.fact.append((self.fact[-1] * i) % self.MOD)
            self.inv.append((-self.inv[self.MOD % i] * (self.MOD // i)) % self.MOD)
            self.factinv.append((self.factinv[-1] * self.inv[-1]) % self.MOD)

    def cmb(self, n: int, r: int, p: int):
        """
        2項係数nCrをpで割った余りを返す
        Parameters
        ----------
        n:int
        r:int
        p:int(法)
        """
        if (r < 0) or (n < r):
            return 0
        r = min(r, n - r)
        return self.fact[n] * self.factinv[r] * self.factinv[n - r] % p

    def Hom(self, n: int, r: int, p: int):
        """
        重複組み合わせnHrをpで割った余りを返す
        Parameters
        ----------
        n:int
        r:int
        p:int(法)
        """
        return self.cmb(n + r - 1, r, p)


N, K = map(int, input().split())
Bin = BinomialCoefficient()
MOD = 1000000007
ans = Bin.Hom(N, K, MOD)
if K >= N:
    ans = Bin.cmb(N, K % N, MOD)
print(ans)
