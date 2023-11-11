from random import random, choice
import sys


def solve():
    N, M = map(int, input().split())
    B = [[] for _ in range(M)]
    S = [set() for _ in range(M)]
    # 箱の格納
    for i in range(M):
        bij = list(map(int, input().split()))
        for b in bij:
            B[i].append(b)
            S[i].add(b)
    # 操作列
    ans = []
    # 小さい方から順に行う
    for v in range(N):
        target = v + 1
        # どの山にあるか探索
        idx = -1
        for i in range(M):
            if target in S[i]:
                idx = i
                break
        # その山のどの位置にあるか探索
        for j, w in enumerate(B[idx]):
            if w == target:
                break
        if B[idx][-1] == w:
            ans.append((target, 0))
            B[idx].pop()
            S[idx].discard(target)
            continue
        # どこに移動させるか
        l = []
        for k in range(M):
            if k == idx:
                continue
            l.append(k)
        dest = choice(l)
        border = B[idx][j + 1]
        ans.append((border, dest + 1))
        # 実際の移動
        stack = []
        while B[idx]:
            p = B[idx].pop()
            S[idx].discard(p)
            if p == target:
                break
            stack.append(p)
        while stack:
            p = stack.pop()
            B[dest].append(p)
            S[dest].add(p)
        ans.append((target, 0))
    for c in ans:
        print(*c)


# 表示内容の出力をファイルに変更
sys.stdout = open("AHC026.log", "w")

solve()
# ファイルを閉じて標準出力を元に戻す
sys.stdout.close()
sys.stdout = sys.__stdout__
