from itertools import groupby
S = list(input())
B = [(k, len(list(v))) for k, v in groupby(S)]
ans = 0
for i in range(len(B)):
    tmp_min = []
    if 0 <= i-1 and B[i-1][0] == 'J':
        tmp_min.append(B[i-1][1])
    if i+1 < len(B) and B[i+1][0] == 'I':
        tmp_min.append(B[i+1][1])
    if len(tmp_min) == 2 and B[i][0] == 'O':
        if B[i][1] <= min(tmp_min):
            ans = max(ans, B[i][1])
print(ans)
