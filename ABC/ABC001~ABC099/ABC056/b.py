W, a, b = map(int, input().split())
if b < a:
    a, b = b, a
if max(a, b) <= min(a + W, b + W):
    exit(print(0))
ans = b - (a + W)
print(ans)
