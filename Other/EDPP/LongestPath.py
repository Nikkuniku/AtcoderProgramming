#Longest Path 

import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = sys.stdin.readline

N,M = map(int,input().split())

dp = [-1]*N
adg_list = [ [] for _ in range(N)]

for i in range(M):
    x,y = map(int,input().split())
    adg_list[x-1].append(y-1)

# print(*dp,sep="\n")
# print(*adg_list,sep="\n")

def rec(v):
    if dp[v] !=-1:
        return dp[v]
    
    nv_s = adg_list[v]

    ans = 0
    #もしnv_s(隣接する頂点の集合)が0の場合は
    #forループは実行されずに0が出力される。
    for nv in nv_s:
        ans = max(ans , rec(nv) + 1)
    dp[v] = ans
    return dp[v]

ans = 0
for w in range(N):
    ans =max(ans,rec(w))
print(ans)


