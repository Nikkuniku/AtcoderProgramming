import sys
import math
# input処理を高速化する
input = sys.stdin.readline

S,W =map(int,input().split())

if S<=W:
    print('unsafe')
else:
    print('safe')