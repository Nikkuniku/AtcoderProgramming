H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
# 横
ans = []
for i in range(H):
    for j in range(W):
        tmp = []
        for k in range(5):
            if j+k >= W:
                break
            tmp.append(S[i][j+k])
        if len(tmp) != 5:
            continue
        tmp_str = ''.join(tmp)
        if tmp_str == 'snuke' or tmp_str == 'ekuns':
            for k in range(5):
                ans.append((i+1, j+k+1))
            if tmp_str == 'ekuns':
                ans = ans[::-1]
            for a in ans:
                print(*a)
            exit()
# 縦
ans = []
for i in range(H):
    for j in range(W):
        tmp = []
        for k in range(5):
            if i+k >= H:
                break
            tmp.append(S[i+k][j])
        if len(tmp) != 5:
            continue
        tmp_str = ''.join(tmp)
        if tmp_str == 'snuke' or tmp_str == 'ekuns':
            for k in range(5):
                ans.append((i+k+1, j+1))
            if tmp_str == 'ekuns':
                ans = ans[::-1]
            for a in ans:
                print(*a)
            exit()
# 斜め(右下)
for i in range(H):
    for j in range(W):
        tmp = []
        for k in range(5):
            if i+k >= H or j+k >= W:
                break
            tmp.append(S[i+k][j+k])
        if len(tmp) != 5:
            continue
        tmp_str = ''.join(tmp)
        if tmp_str == 'snuke' or tmp_str == 'ekuns':
            for k in range(5):
                ans.append((i+k+1, j+k+1))
            if tmp_str == 'ekuns':
                ans = ans[::-1]
            for a in ans:
                print(*a)
            exit()
# 斜め(左下)
for i in range(H):
    for j in range(W):
        tmp = []
        for k in range(5):
            if i+k >= H or j-k < 0:
                break
            tmp.append(S[i+k][j-k])
        if len(tmp) != 5:
            continue
        tmp_str = ''.join(tmp)
        if tmp_str == 'snuke' or tmp_str == 'ekuns':
            for k in range(5):
                ans.append((i+k+1, j-k+1))
            if tmp_str == 'ekuns':
                ans = ans[::-1]
            for a in ans:
                print(*a)
            exit()
