A, B = map(int, input().split())
ans = "Alloy"
if 0 < A and B == 0:
    ans = "Gold"
elif A == 0 and B > 0:
    ans = "Silver"
print(ans)
