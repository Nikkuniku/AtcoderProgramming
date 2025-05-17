class BinomialCoefficient:
    def __init__(self) -> None:
        self.MOD = 1000000007
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


def sum_area(i, j):
    return i * j * (i + j + 2) // 2


def sum_line(k):
    return k * (k + 1) // 2


binomial = BinomialCoefficient()
N, M, K = map(int, input().split())
ans = 0

for i in range(N):
    for j in range(M):
        A = [i, N - 1 - i]
        B = [j, M - 1 - j]
        temp = 0
        for a in A:
            for b in B:
                temp += sum_area(a, b)
                temp %= binomial.MOD
        for a in A:
            temp += sum_line(a)
            temp %= binomial.MOD
        for b in B:
            temp += sum_line(b)
            temp %= binomial.MOD
        ans += temp
        ans %= binomial.MOD
ans *= pow(2, -1, binomial.MOD)
ans *= binomial.cmb(N * M - 2, K - 2)
ans %= binomial.MOD
print(ans)
