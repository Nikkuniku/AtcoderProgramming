S = input()
ans = 'Yes'
if len(S) != 8:
    print('No')
    exit()

a = S[0]
b = S[1:7]
c = S[7:]
if not b.isnumeric():
    ans = 'No'
else:
    if len(str(int(b))) != 6:
        ans = 'No'
if not a.isalpha() or not c.isalpha():
    ans = 'No'

print(ans)
