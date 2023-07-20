N = int(input())
S = input()
S = S.replace('.', '')
ans = 'out'
if S == '|*|':
    ans = 'in'
print(ans)
