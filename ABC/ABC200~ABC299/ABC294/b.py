H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
ans = [['.']*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if A[i][j] == 0:
            continue
        ans[i][j] = chr(64+A[i][j])
for a in ans:
    print(''.join(a))
