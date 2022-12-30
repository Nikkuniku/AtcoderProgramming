import sys
import math

from collections import Counter

# input処理を高速化する
input = sys.stdin.readline

N=int(input())
Keihin =[]
for i in range(N):
    syouhin = input()
    Keihin.append(syouhin)

c=Counter(Keihin)
print(len(list(c.keys())))