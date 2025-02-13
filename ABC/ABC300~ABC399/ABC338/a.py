from string import ascii_lowercase, ascii_uppercase

S = input()
ans = "Yes"
if S[0] in ascii_lowercase:
    ans = "No"
for i in range(1, len(S)):
    if S[i] in ascii_uppercase:
        ans = "No"
print(ans)
