S = input()
ans = "No"
if S[0] == S[0].upper() and S[1:] == S[1:].lower():
    ans = "Yes"
print(ans)
