N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
ans = []
for i in range(N-9+1):
    for j in range(M-9+1):
        # 左上3*3マス
        isOK = True
        for a in range(3):
            for b in range(3):
                if S[i+a][j+b] == '.':
                    isOK = False
        # 右下3*3マス
        for a in range(6, 9):
            for b in range(6, 9):
                if S[i+a][j+b] == '.':
                    isOK = False
        # 左上白ます
        for a in range(4):
            for b in range(4):
                if a < 3 and b < 3:
                    continue
                if S[i+a][j+b] == '#':
                    isOK = False
        # 右下白ます
        for a in range(5, 9):
            for b in range(5, 9):
                if 5 < a and 5 < b:
                    continue
                if S[i+a][j+b] == '#':
                    isOK = False
        if isOK:
            ans.append((i+1, j+1))
for c in sorted(ans):
    print(*c)
