A, B, C = map(int, input().split())
D = set([i for i in range(24)])
if B < C:
    for t in range(B, C + 1):
        D.discard(t)
else:
    for t in range(B, 25):
        D.discard(t)
    for t in range(0, C + 1):
        D.discard(t)
ans = "No"
if A in D:
    ans = "Yes"
print(ans)
