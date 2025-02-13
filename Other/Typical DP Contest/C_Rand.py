from random import randint
import sys

K = int(input())
res = []
for _ in range(1 << K):
    res.append(randint(0, 4000))
# 表示内容の出力をファイルに変更
sys.stdout = open("TDPC_C.log", "w")
print(*res, sep="\n")
# ファイルを閉じて標準出力を元に戻す
sys.stdout.close()
sys.stdout = sys.__stdout__
