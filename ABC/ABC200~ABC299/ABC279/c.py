H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]
colS = []
for j in range(W):
    tmp = []
    for i in range(H):
        tmp.append(S[i][j])
    colS.append(tmp)
colT = []
for j in range(W):
    tmp = []
    for i in range(H):
        tmp.append(T[i][j])
    colT.append(tmp)
colS.sort()
colT.sort()
ans = 'No'
if colS == colT:
    ans = 'Yes'
print(ans)
