import sys
import math
# input処理を高速化する
input = sys.stdin.readline

N=int(input())

q,mod = divmod(N,2)

print(q+mod)