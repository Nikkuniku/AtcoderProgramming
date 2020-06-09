import sys
import numpy as np
# input処理を高速化する
input = sys.stdin.readline

L=int(input())

#forループではない
# div =0.001
# ranges =np.arange(0.001,L+1,0.01)
# V=0
# for x in ranges:
#     z=L-2*x
#     V=max(V,x*x*z)

# print(V)
#相加相乗平均を用いる
print((L/3)**3)