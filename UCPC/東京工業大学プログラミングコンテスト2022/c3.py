import sys
def input(): return sys.stdin.readline()[:-1]


N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))
E = list(map(int, input().split()))


mod = 998244353

P = sorted(list(zip(A, [0] * N))+list(zip(B, [1] * N)) +
           list(zip(C, [2] * N))+list(zip(D, [3] * N))+list(zip(E, [4] * N)))

left = [0, 0, 0, 0, 0]
ans = 0
for i in range(N*5):
    f = [0, 1, 2, 3, 4]
    f.remove(P[i][1])
    ans += P[i][0] * left[f[0]] % mod * left[f[1]] % mod * \
        (N - left[f[2]]) % mod * (N - left[f[3]]) % mod
    ans %= mod
    ans += P[i][0] * left[f[0]] % mod * left[f[2]] % mod * \
        (N - left[f[1]]) % mod * (N - left[f[3]]) % mod
    ans %= mod
    ans += P[i][0] * left[f[0]] % mod * left[f[3]] % mod * \
        (N - left[f[1]]) % mod * (N - left[f[2]]) % mod
    ans %= mod
    ans += P[i][0] * left[f[1]] % mod * left[f[2]] % mod * \
        (N - left[f[0]]) % mod * (N - left[f[3]]) % mod
    ans %= mod
    ans += P[i][0] * left[f[1]] % mod * left[f[3]] % mod * \
        (N - left[f[0]]) % mod * (N - left[f[2]]) % mod
    ans %= mod
    ans += P[i][0] * left[f[2]] % mod * left[f[3]] % mod * \
        (N - left[f[0]]) % mod * (N - left[f[1]]) % mod
    ans %= mod
    left[P[i][1]] += 1

print(ans)
