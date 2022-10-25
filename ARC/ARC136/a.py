n = int(input())
s = input()

s = s.replace('A', 'BB')

ans = []
for i in range(len(s)):
    ans.append(s[i])
    if len(ans) >= 2:
        if ans[-2] == 'B' and ans[-1] == 'B':
            ans.pop()
            ans.pop()
            ans.append('A')
print(''.join(ans))
