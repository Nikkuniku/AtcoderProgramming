W, H = map(int, input().split())
ans = 1
MOD = 10**9 + 7


def inv(k):
    return pow(k, MOD-2, MOD)


for i in range(1, H+W-2+1):
    ans *= i
    ans %= MOD

for i in range(1, H):
    ans *= inv(i)
    ans %= MOD
for i in range(1, W):
    ans *= inv(i)
    ans %= MOD
print(ans)
