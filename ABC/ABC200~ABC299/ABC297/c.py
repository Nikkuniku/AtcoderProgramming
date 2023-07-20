H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
for i in range(H):
    for j in range(W-1):
        if S[i][j] == S[i][j+1] == 'T':
            S[i][j] = 'P'
            S[i][j+1] = 'C'
for c in S:
    print(''.join(c))
