N = int(input())
S = input()
ans = "No"
if S.count("o") > 0 and S.count("x") == 0:
    ans = "Yes"
print(ans)
