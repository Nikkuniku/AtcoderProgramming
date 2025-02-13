S = input()
ans = "Yes"
if S[0] != "<" or S[-1] != ">":
    ans = "No"
for i in range(1, len(S) - 1):
    if S[i] != "=":
        ans = "No"
print(ans)
