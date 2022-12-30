N = int(input())
S = input()
ans = []
Flg = False
for i in range(N):
    if S[i] == ',':
        if not Flg:
            ans.append('.')
        else:
            ans.append(',')
    else:
        ans.append(S[i])
        if S[i] == '"':
            Flg ^= 1
print(''.join(ans))
