A, B, C = map(int, input().split())
if A % 2 != 0 or B % 2 != 0 or C % 2 != 0:
    exit(print(0))
if A == B == C:
    exit(print(-1))
ans = 0
while A % 2 == 0 and B % 2 == 0 and C % 2 == 0:
    A, B, C = (B + C) // 2, (A + C) // 2, (A + B) // 2
    ans += 1
print(ans)
