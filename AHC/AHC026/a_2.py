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
        # 既に上にあるならば、除く
        if B[idx][-1] == w:
            ans.append((target, 0))
            B[idx].pop()
            S[idx].discard(target)
            continue

        # どこに移動させるか
        # borderより大きい値であって、距離が近いもののところに置く
        border = B[idx][j + 1]
        kouho = []
        dest = 0
        for k in range(M):
            if k == idx:
                continue
            if not B[k]:
                kouho.append((100, k))
            for s in range(len(B[k]) - 1, -1, -1):
                if border < B[k][s]:
                    kouho.append((70 * (len(B[k]) - s) + 30 * len(B[k]), k))
                    break
                    # kouho.append(((len(B[k]) - s), k))
        kouho.sort(reverse=True)
        dest = kouho[0][1]
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
