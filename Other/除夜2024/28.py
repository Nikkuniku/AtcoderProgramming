a, b = map(int, input().split())
S = set()
S.add(b + (b - a))
S.add(a - (b - a))
S.add(a + (a - b))
S.add(b - (a - b))
if (a + b) % 2 == 0:
    S.add((a + b) // 2)
print(len(S))
