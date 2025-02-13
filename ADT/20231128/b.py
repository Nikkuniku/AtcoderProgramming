N = int(input())
S = input()
ans = "No"
if S.count("o") and not S.count("x"):
    ans = "Yes"
print(ans)
