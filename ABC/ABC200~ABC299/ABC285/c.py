from string import ascii_uppercase
S = input()
ans = 0
S = S[::-1]
for i in range(len(S)):
    j = ascii_uppercase.index(S[i])+1
    ans += j*pow(26, i)
print(ans)
