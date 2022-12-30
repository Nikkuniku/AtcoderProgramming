N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
mod = 10**9 + 7
# xの逆元を求める。フェルマーの小定理より、 x の逆元は x ^ (mod - 2) に等しい。計算時間はO(log(mod))程度。
# https://qiita.com/Yaruki00/items/fd1fc269ff7fe40d09a6


def modinv(x):
    return pow(x, mod-2, mod)

# 二項係数の左側の数字の最大値を max_len　とする。nとかだと他の変数と被りそうなので。
# factori_table = [1, 1, 2, 6, 24, 120, ...] 要は factori_table[n] = n!
# 計算時間はO(max_len * log(mod))


max_len = N

factori_table = [1] * (max_len + 1)
factori_inv_table = [1] * (max_len + 1)
for i in range(1, max_len + 1):
    factori_table[i] = factori_table[i-1] * (i) % mod
    factori_inv_table[i] = modinv(factori_table[i])


def binomial_coefficients(n, k):
    # n! / (k! * (n-k)! )
    return factori_table[n] * factori_inv_table[k] * factori_inv_table[n-k]


ans = 0
for i in range(N-K+1):
    ans -= binomial_coefficients(N-(i+1), K-1)*A[i]
    ans %= mod
for i in range(K-1, N):
    ans += binomial_coefficients(i, K-1)*A[i]
    ans %= mod
print(ans)
