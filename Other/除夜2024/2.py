a, b = map(int, input().split())
s = set(range(10))
s.discard(a + b)
print(min(s))
