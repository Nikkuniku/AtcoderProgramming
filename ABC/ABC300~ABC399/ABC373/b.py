from string import ascii_uppercase

S = input()
j = S.index("A")
ans = 0
for i in range(1, len(ascii_uppercase)):
    next = ascii_uppercase[i]
    ans += abs(S.index(next) - j)
    j = S.index(next)
print(ans)
