import sys
from collections import defaultdict


def solve():
    N, M = map(int, input().split())
    si, sj = map(int, input().split())
    A = [list(input()) for _ in range(N)]
    d = defaultdict(list)
    for i in range(N):
        for j in range(N):
            d[A[i][j]].append((i, j))

    def search(s, ni, nj):
        res = []
        for x, y in d[s]:
            tmp = abs(ni - x) + abs(nj - y) + 1
            res.append((tmp, x, y))
        res.sort()
        return res[0][1], res[0][2]

    ans = []
    for _ in range(M):
        t = input()
        for s in t:
            x, y = search(s, si, sj)
            ans.append((x, y))
            si, sj = x, y

    for c in ans:
        print(*c)


# 表示内容の出力をファイルに変更
sys.stdout = open("AHC028.log", "w")

solve()
# ファイルを閉じて標準出力を元に戻す
sys.stdout.close()
sys.stdout = sys.__stdout__
