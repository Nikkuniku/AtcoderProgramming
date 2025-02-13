A, B, C = map(int, input().split())
ans = "!"
if A + B == C and A - B == C:
    ans = "?"
elif A + B == C and A - B != C:
    ans = "+"
elif A + B != C and A - B == C:
    ans = "-"
print(ans)
