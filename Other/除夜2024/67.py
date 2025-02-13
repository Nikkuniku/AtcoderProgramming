from string import ascii_uppercase

S = input()
cnt = 0
for s in S:
    cnt += s in ascii_uppercase
if cnt > len(S) // 2:
    S = S.upper()
else:
    S = S.lower()
print(S)
