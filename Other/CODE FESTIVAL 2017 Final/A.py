d = {1: 'K', 2: 'I', 3: 'H', 5: 'B', 7: 'R'}
S = ['']
for i in range(9):
    tmp = []
    if i not in d:
        for s in S:
            tmp.append(s+'')
            tmp.append(s+'A')
    else:
        for s in S:
            tmp.append(s+d[i])
    S, tmp = tmp, S
IS = input()
print('YES' if IS in S else 'NO')
