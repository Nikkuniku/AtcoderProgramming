def trimming(A):
    res = []
    for s in A:
        if "".join(s) == "." * len(s):
            continue
        res.append(s)
    res2 = [[] for _ in range(len(res))]
    for j in range(W):
        tmp = []
        for i in range(len(res)):
            tmp.append(res[i][j])
        if "".join(tmp) == "." * len(res):
            continue
        for i in range(len(res)):
            res2[i].append(res[i][j])
    return res2


def matrix_rotate90degree_toright(A: list) -> list:
    """
    2次元リストの90度右回転
    Parameters
    ----------
    A:any[][]
    """
    return [list(x) for x in zip(*A[::-1])]


def check(S, T, s, t):
    p = len(T)
    q = len(T[0])
    for i in range(p):
        for j in range(q):
            if not (0 <= s + i < H and 0 <= t + j < W):
                return False
            if S[s + i][t + j] == "#" and T[i][j] == "#":
                return False
    return True


H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = [list(input()) for _ in range(H)]
T = trimming(T)

ans = "No"
for h in range(H):
    for w in range(W):
        for _ in range(4):
            T = matrix_rotate90degree_toright(T)
            if check(S, T, h, w):
                ans = "Yes"
                break
print(ans)
