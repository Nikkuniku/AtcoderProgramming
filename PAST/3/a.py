s = input()
t = input()
ans = "different"
if s == t:
    ans = "same"
elif s.upper() == t.upper():
    ans = "case-insensitive"
print(ans)
