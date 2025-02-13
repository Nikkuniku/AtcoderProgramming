a, b = map(int, input().split())
ans = set()
d = b - a
ans.add(b + d)
d = a - b
ans.add(a + d)
d = b - a
ans.add(a - d)
d = a - b
ans.add(b - d)
if (b + a) % 2 == 0:
    ans.add((a + b) // 2)
print(len(ans))
