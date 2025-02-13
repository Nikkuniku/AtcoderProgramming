N, T, A = map(int, input().split())
M = N - (T + A)
ans = "No"
if T > A:
    if T > A + M:
        ans = "Yes"
else:
    if A > T + M:
        ans = "Yes"
print(ans)
