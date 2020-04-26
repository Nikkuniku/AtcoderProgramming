import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = sys.stdin.readline

K,S = map(int,input().split())
cnt = 0

for x in range(K+1):
    for y in range(K+1):
        z =S - x - y
        if z <=K and z>=0:
            cnt +=1

print(cnt)