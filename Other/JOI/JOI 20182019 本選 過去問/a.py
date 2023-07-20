H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
Orb = [[0]*W for _ in range(H)]
Ingot = [[0]*W for _ in range(H)]
C_Orb = [[0] for _ in range(H)]
C_Ingot = [[0] for _ in range(W)]
for i in range(H):
    for j in range(W):
        if S[i][j] == 'O':
            Orb[i][j] += 1
        if S[i][j] == 'I':
            Ingot[i][j] += 1
for i in range(H):
    for j in range(W):
        C_Orb[i].append(C_Orb[i][-1]+Orb[i][j])
for j in range(W):
    for i in range(H):
        C_Ingot[j].append(C_Ingot[j][-1]+Ingot[i][j])
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == 'J':
            p = C_Orb[i][-1]-C_Orb[i][j+1]
            q = C_Ingot[j][-1]-C_Ingot[j][i+1]
            ans += p*q
print(ans)
