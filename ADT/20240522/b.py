l1, r1, l2, r2 = map(int, input().split())
Line = [0] * 102
for i in range(l1, r1 + 1):
    Line[i] += 1
for i in range(l2, r2 + 1):
    Line[i] += 1
if Line.count(2) == 0:
    ans = 0
else:
    ans = Line.count(2) - 1
print(ans)
