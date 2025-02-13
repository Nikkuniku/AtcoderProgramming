from string import ascii_lowercase

N, L = map(int, input().split())
S = [set(list(input())) for _ in range(N)]
ans = 0
MOD = 998244353
for i in range(1, 1 << N):
    tmp = set(list(ascii_lowercase))
    cnt = 0
    for j in range(N):
        if i & (1 << j):
            tmp &= S[j]
            cnt += 1
    if cnt % 2 == 0:
        ans -= pow(len(tmp), L, MOD)
    else:
        ans += pow(len(tmp), L, MOD)
    ans %= MOD
print(ans)
