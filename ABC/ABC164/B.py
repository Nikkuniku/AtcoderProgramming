import sys
import math
# input処理を高速化する
input = sys.stdin.readline

A,B,C,D = map(int,input().split())

while True:
    C=C-B
    if C<=0:
        print('Yes')
        exit(0)
    A=A-D
    if A<=0:
        print('No')
        exit(0)