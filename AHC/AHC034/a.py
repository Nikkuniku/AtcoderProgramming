import sys

N = int(input())
H = [list(map(int, input().split())) for _ in range(N)]
ans = []
x, y = 0, 0
while 1:
    # 各マスの高さを調べる
    Sands = []
    for i in range(N):
        for j in range(N):
            if H[i][j] <= 0:
                continue
            Sands.append((H[i][j], abs(i - x) + abs(j - y), i, j))
    if not Sands:
        break
    Sands.sort(key=lambda x: x[0], reverse=True)
    Sands.sort(key=lambda x: x[1])
    d = Sands[0][0]
    px, py = Sands[0][2:]
    for _ in range(abs(x - px)):
        if x - px > 0:
            ans.append("U")
        else:
            ans.append("D")
    for _ in range(abs(y - py)):
        if y - py > 0:
            ans.append("L")
        else:
            ans.append("R")
    x, y = px, py
    ans.append("+{}".format(d))
    H[px][py] = 0
    while d:
        Negs = []
        for i in range(N):
            for j in range(N):
                if H[i][j] >= 0:
                    continue
                Negs.append((H[i][j], abs(i - x) + abs(j - y), i, j))
        Negs.sort(key=lambda x: x[1])
        target = Negs[0][0]
        qx, qy = Negs[0][2:]
        for _ in range(abs(x - qx)):
            if x - qx > 0:
                ans.append("U")
            else:
                ans.append("D")
        for _ in range(abs(y - qy)):
            if y - qy > 0:
                ans.append("L")
            else:
                ans.append("R")
        x, y = qx, qy
        if d + target >= 0:
            d += target
            H[qx][qy] = 0
            ans.append("{}".format(target))
        else:
            H[qx][qy] += d
            ans.append("-{}".format(d))
            d = 0

# 表示内容の出力をファイルに変更
sys.stdout = open("AHC034.log", "w")
print(*ans, sep="\n")
# ファイルを閉じて標準出力を元に戻す
sys.stdout.close()
sys.stdout = sys.__stdout__
