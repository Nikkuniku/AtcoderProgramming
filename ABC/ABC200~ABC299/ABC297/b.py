S = input()
N = len(S)
ans = 'Yes'
# B
b = []
for i in range(N):
    if S[i] == 'B':
        b.append(i)
if b[0] % 2 == b[1] % 2:
    ans = 'No'
# KR
s = []
for i in range(N):
    if S[i] == 'K' or S[i] == 'R':
        s.append(S[i])
if ''.join(s) != 'RKR':
    ans = 'No'
print(ans)
