import sys
# input処理を高速化する
input = sys.stdin.readline

S=input()

cnt_a = S.count('A')
cnt_b = S.count('B')

if cnt_a>0 and cnt_b>0:
    print('Yes')
else:
    print('No')