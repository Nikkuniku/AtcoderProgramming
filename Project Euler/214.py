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


def totient(n: int) -> int:
    """
    オイラーのphi関数
    1以上n以下の数でnと互いに素な数の個数
    Parameters
    ----------
    n:int
    """
    arr = []
    temp = n
    for i in range(2, int(-(-(n**0.5) // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append((i, cnt))

    if temp != 1:
        arr.append((temp, 1))

    if arr == []:
        arr.append((n, 1))
    res = n
    for p, _ in arr:
        res = res * (p - 1) // p
    return res


N = 40000000
M = 25
ER = eratosthenes(N + 1)
ans = 0
res = [1] * (N + 1)
memo = [-1] * (N + 1)
memo[0] = memo[1] = 1
for i in range(2, N + 1):
    if ER.isprime[i]:
        memo[i] = i - 1
        q = i - 1
    else:
        factors = ER.factorize(i)
        q = 1
        for p, e in factors:
            if memo[p**e] == -1:
                b = totient(p**e)
                memo[p**e] = b
            else:
                b = memo[p**e]
            q *= b
    res[i] = res[q] + 1
    if ER.isprime[i] and res[i] == M:
        ans += i
print(ans)
