S = list(input())
p, s = 0, 0
while S and S[-1] == "a":
    s += 1
    S.pop()
S = S[::-1]
while S and S[-1] == "a":
    p += 1
    S.pop()
ans = "No"
if S == S[::-1] and p <= s:
    ans = "Yes"
print(ans)
