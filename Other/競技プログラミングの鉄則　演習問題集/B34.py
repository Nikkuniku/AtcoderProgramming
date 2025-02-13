N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
xorsum = 0
for a in A:
    xorsum ^= (a % 5) // 2
ans = "First" if xorsum else "Second"
print(ans)
