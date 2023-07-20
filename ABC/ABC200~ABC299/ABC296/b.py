S = [list(input()) for _ in range(8)]
ni = -1
nj = -1
for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            ni = i
            nj = j
yoko = 'abcdefgh'
tate = '12345678'
ans = yoko[nj]+tate[7-ni]
print(ans)
