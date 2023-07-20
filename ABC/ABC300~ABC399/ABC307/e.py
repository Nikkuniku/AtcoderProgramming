N, M = map(int, input().split())
MOD = 998244353
ans = 1
if M == 2:
    if N % 2 == 0:
        ans = 2
    else:
        ans = 0
else:
    if N == 2:
        ans = M*(M-1)
    elif N == 3:
        ans = M*(M-1)*(M-2)
    else:
        ans = M*(M-1)*pow((M-2), N-4, MOD)*(M-4)*(M-4)
ans %= MOD
print(ans)
