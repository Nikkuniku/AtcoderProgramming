from string import ascii_uppercase, ascii_lowercase

S = input()
ans = "Yes"
if len(set(list(S))) != len(S):
    ans = "No"
if not any([s in S for s in ascii_uppercase]):
    ans = "No"
if not any([s in S for s in ascii_lowercase]):
    ans = "No"
print(ans)
