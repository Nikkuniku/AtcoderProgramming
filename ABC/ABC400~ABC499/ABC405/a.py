R, X = map(int, input().split())
ans = "No"
if X == 1:
    if 1600 <= R <= 2999:
        ans = "Yes"
else:
    if 1200 <= R <= 2399:
        ans = "Yes"
print(ans)
