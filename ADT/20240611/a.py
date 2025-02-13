X, Y = input().split(".")
ans = X
Y = int(Y)
if 0 <= Y <= 2:
    ans += "-"
if 7 <= Y <= 9:
    ans += "+"
print(ans)
