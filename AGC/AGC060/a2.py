from string import ascii_lowercase
N = int(input())
S = input()
dp = [26]*N
MOD = 998244353
for i in range(N):
    if S[i] in ascii_lowercase:
        dp[i] = 1
        for j in [-2, -1, 1, 2]:
            k = i+j
            if 0 <= k < N:
                if S[k] == S[i]:
                    dp[k] = 0
                elif S[k] not in ascii_lowercase:
                    dp[k] -= 1

for i in range(N):
    if S[i] in ascii_lowercase:
        continue
    lq = 0
    for j in [-2, -1]:
        k = i+j
        if 0 <= k < N:
            if S[k] == '?':
                lq += 1
    dp[i] -= lq
ans = 1
for c in dp:
    ans *= c
    ans %= MOD
print(dp)
print(ans)
