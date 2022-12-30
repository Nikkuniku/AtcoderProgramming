N = int(input())
A = [sorted(list(map(int, input().split()))) for _ in range(5)]
t = []
for i in range(5):
    for j in range(N):
        t.append((A[i][j], i))
left, right = [0]*5, [N]*5
t.sort()
ans = 0
MOD = 998244353
for v, p in t:
    f = [0, 1, 2, 3, 4]
    f.remove(p)
    ans += (v*left[f[0]]*left[f[1]]*right[f[2]]*right[f[3]]) % MOD
    ans += (v*left[f[0]]*left[f[2]]*right[f[1]]*right[f[3]]) % MOD
    ans += (v*left[f[0]]*left[f[3]]*right[f[1]]*right[f[2]]) % MOD
    ans += (v*left[f[1]]*left[f[2]]*right[f[0]]*right[f[3]]) % MOD
    ans += (v*left[f[1]]*left[f[3]]*right[f[0]]*right[f[2]]) % MOD
    ans += (v*left[f[2]]*left[f[3]]*right[f[0]]*right[f[1]]) % MOD
    ans %= MOD
    left[p] += 1
    right[p] -= 1
print(ans)
