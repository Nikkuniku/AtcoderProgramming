import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
MOD = 1000000007
ans = 0
p = 60
bits = [0 for _ in range(p)]
pows = []
for i in range(60):
    pows.append(pow(2, i, MOD))

for i in range(1, n):
    for j in range(p):
        if a[i-1] & (1 << j):
            bits[j] += 1

    for j in range(p):
        if a[i] & (1 << j):
            k = (i % MOD) - (bits[j] % MOD)
        else:
            k = bits[j]
        ans = (ans + pows[j]*(k % MOD)) % MOD
print(ans)


# def solve1():
#     ans = 0
#     for i in range(n):
#         for j in range(i+1, n):
#             ans += a[i] ^ a[j]
#             ans %= MOD
#     return ans


# print(solve1())
