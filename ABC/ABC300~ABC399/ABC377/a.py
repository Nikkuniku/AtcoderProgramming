S = list(input())
S.sort()
ans = "No"
if "".join(S) == "ABC":
    ans = "Yes"
print(ans)
