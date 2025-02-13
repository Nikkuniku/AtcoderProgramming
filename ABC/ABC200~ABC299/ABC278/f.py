from functools import cache

N = int(input())
S = [input() for _ in range(N)]


@cache
def dp(s, j):
    if s == (1 << N) - 1:
        return False
    res = []
    # 最初
    if s == 0:
        for i in range(N):
            res.append(dp(s | (1 << i), i))
    # 最初以外
    else:
        for i in range(N):
            if s & (1 << i):
                continue
            if S[j][-1] == S[i][0]:
                res.append(dp(s | (1 << i), i))
    # 遷移できない場合は負け
    if not res:
        return False
    # 全て勝ちの状態に遷移する場合は負け
    if all(res):
        return False
    return True


ans = "First" if dp(0, 0) else "Second"
print(ans)
