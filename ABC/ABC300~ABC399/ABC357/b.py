from string import ascii_lowercase, ascii_uppercase

U = 0
L = 0
S = input()
for s in S:
    if s in ascii_lowercase:
        L += 1
    if s in ascii_uppercase:
        U += 1
if U > L:
    ans = S.upper()
else:
    ans = S.lower()
print(ans)
