n = int(input())
s = input()
ans = 'No'
if n == 2:
    if s in ['AA', 'BB']:
        ans = 'Yes'
else:
    if s == s[::-1]:
        ans = 'Yes'
    else:
        if s[-1] == 'A':
            ans = 'Yes'
        elif s[0] == 'B' and s[-1] == 'B':
            ans = 'Yes'
print(ans)
