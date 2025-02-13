from string import ascii_uppercase

S = input()
ans = 0
now = 0
for i in range(len(ascii_uppercase)):
    alphabet = ascii_uppercase[i]
    if i == 0:
        now = S.index(alphabet)
    else:
        j = S.index(alphabet)
        ans += abs(now - j)
        now = j
print(ans)
