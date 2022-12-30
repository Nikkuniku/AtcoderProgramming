s = input()
apper = False
lower = False
length = False
for i in range(len(s)):
    if s[i].isupper():
        apper = True
for i in range(len(s)):
    if s[i].islower():
        lower = True

p = set(list(s))
if len(p) == len(s):
    length = True

ans = 'No'
if apper and lower and length:
    ans = 'Yes'
print(ans)
