N, L, R = map(int, input().split())
A = list(map(int, input().split()))
xorsum = 0
for a in A:
    xorsum ^= (a % (L + R)) // L
ans = "First" if xorsum else "Second"
print(ans)
