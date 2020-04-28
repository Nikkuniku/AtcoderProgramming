import sys
# input処理を高速化する
input = sys.stdin.readline

N,X,Y = map(int,input().split())

# dp =[[0]*(N) for _ in range(N)]
# for j in range(N-1):
#     dp[j][j+1]=1
#     dp[j+1][j]=1

# # 線がついているところ
# dp[X-1][Y-1] = 1
# dp[Y-1][X-1] = 1

# print(*dp,sep="\n")

def dist(s,g):
    if s<=X and Y<=g:
        return X-s + 1 + g-Y
    elif s==X and g==Y:
        return 1
    else:
        return min(g-s,abs(s-X)+1+abs(g-Y),abs(s-Y)+1+abs(g-X))

# for k in range(1,N):
#     cnt =0

#     if k==1:
#         print(N)
#     else:
#         for i in range(1,N+1):
#             for j in range(i+1,N+1):
#                 if dist(i,j) == k:
#                     cnt+=1
#         print(cnt)


d =[0]*N



