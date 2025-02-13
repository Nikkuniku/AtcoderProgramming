A, B, a, b = map(int, input().split())
ans = -1
for x in range(A * B + 1):
    if x % A == a and x % B == b:
        ans = x
        break
print(ans)
