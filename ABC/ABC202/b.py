s=list(input())

s=list(reversed(s))

for i in range(len(s)):
    if s[i]=='6':
        s[i]='9'
    elif s[i]=='9':
        s[i]='6'

ans=''.join(s)

print(ans)