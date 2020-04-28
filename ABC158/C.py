import sys
import math
# input処理を高速化する
input = sys.stdin.readline

A,B = map(int,input().split())

Moneys = range(1,1001)

#消費税が入力と一致したインデックス
a_index=set()
b_index=set()

for i in Moneys:
    if math.floor(i*0.08) == A:
        a_index.add(i)

for j in Moneys:
    if math.floor(j*0.1) == B:
        b_index.add(j)

Tax = a_index&b_index

if len(Tax)!=0:
    print(min(list(Tax)))
else:
    print(-1)