from sys import setrecursionlimit

setrecursionlimit(10**8)
A = [list(map(int, input().split())) for _ in range(3)]


def dfs(pattern, turn):
    for i in range(3):
        tmp = set(pattern[i])
        if len(tmp) == 1:
            if min(tmp) == 1:
                return True
            if min(tmp) == 2:
                return False
    for j in range(3):
        tmp = set([pattern[i][j] for i in range(3)])
        if len(tmp) == 1:
            if min(tmp) == 1:
                return True
            if min(tmp) == 2:
                return False
    tmp = set([pattern[0][0], pattern[1][1], pattern[2][2]])
    if len(tmp) == 1:
        if min(tmp) == 1:
            return True
        if min(tmp) == 2:
            return False
    tmp = set([pattern[0][2], pattern[1][1], pattern[2][0]])
    if len(tmp) == 1:
        if min(tmp) == 1:
            return True
        if min(tmp) == 2:
            return False
    # 全部埋まっている時
    isall = True
    tmpt, tmpa = 0, 0
    for i in range(3):
        for j in range(3):
            if pattern[i][j] == 0:
                isall = False
            if pattern[i][j] == 1:
                tmpt += A[i][j]
            if pattern[i][j] == 2:
                tmpa += A[i][j]
    if isall:
        if tmpt > tmpa:
            return True
        else:
            return False

    win_pattern = set()
    for i in range(3):
        for j in range(3):
            if pattern[i][j] == 0:
                if turn % 2 != 0:
                    pattern[i][j] = 1
                    res = dfs(pattern, turn + 1)
                    win_pattern.add(res)
                    pattern[i][j] = 0
                else:
                    pattern[i][j] = 2
                    res = dfs(pattern, turn + 1)
                    win_pattern.add(res)
                    pattern[i][j] = 0
    if turn % 2 != 0:
        if True in win_pattern:
            return True
        else:
            return False
    else:
        if False in win_pattern:
            return False
        else:
            return True


res = dfs([[0] * 3 for _ in range(3)], 1)
ans = "Aoki"
if res:
    ans = "Takahashi"
print(ans)
