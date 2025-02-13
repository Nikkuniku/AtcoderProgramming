N, K = map(int, input().split())
A = list(map(int, input().split()))
xor = 0
for a in A:
    xor ^= a % (K + 1)
ans = "YES" if xor else "NO"
print(ans)
