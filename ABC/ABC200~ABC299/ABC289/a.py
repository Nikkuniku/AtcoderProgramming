s=input()
ans=[]
for i in range(len(s)):
    if s[i]=='0':
        ans.append('1')
    else:
        ans.append('0')
print(''.join(ans))