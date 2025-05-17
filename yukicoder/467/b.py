N = int(input())
S = input()
res = 0
for s in S:
    if s == "(":
        res += 1
    else:
        res -= 1
ans = "Yes" if res == 0 else "No"
print(ans)
