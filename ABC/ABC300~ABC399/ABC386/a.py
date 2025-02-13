S = list(map(int, input().split()))
S = set(S)
ans = "No"
if len(S) == 2:
    ans = "Yes"
print(ans)
