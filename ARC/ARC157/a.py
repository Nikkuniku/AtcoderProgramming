N, A, B, C, D = map(int, input().split())
ans = 'No'
if N == 1:
    ans = 'Yes'
if B > 0 or C > 0:
    if abs(B-C) <= 1:
        ans = 'Yes'
else:
    if A > 0 and D == 0:
        ans = 'Yes'
    elif A == 0 and D > 0:
        ans = 'Yes'
print(ans)
