from collections import Counter


class BinomialCoefficient:
    def __init__(self) -> None:
        self.MOD = 10**9 + 7
        self.N = 2 * 10**6  # N は必要分だけ用意する
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
N = int(input())
A = list(map(int, input().split()))
C = Counter(A)
V = max([v if C[v] == 2 else 0 for v in range(N + 1)])
B = [0, 0, 0]
j = 0
for i, v in enumerate(A):
    if v != V:
        B[j] += 1
    else:
        j += 1
ans = []
MOD = 10**9 + 7
for k in range(1, N + 2):
    tmp = 0
    if k == 1:
        tmp = N
    else:
        # Vを取らない
        tmp += binomial.cmb(sum(B), k)
        # Vを2つ取る
        tmp += binomial.cmb(sum(B), k - 2)
        # Vを一つとる
        tmp += 2 * binomial.cmb(sum(B), k - 1)
        tmp -= binomial.cmb(B[0] + B[2], k - 1)
    ans.append(tmp % MOD)
print(*ans, sep="\n")
