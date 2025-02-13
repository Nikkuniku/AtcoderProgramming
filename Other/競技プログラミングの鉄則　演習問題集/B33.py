N, H, W = map(int, input().split())
A = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    A.append(b)
xorsum = 0
for a in A:
    xorsum ^= a - 1
ans = "First" if xorsum else "Second"
print(ans)
