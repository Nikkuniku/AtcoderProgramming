h,w,k=map(int,input().split())
s=[]
for _ in range(h):
    s.append(list(input()))
ans=[[0]*w for _ in range(h)]
# 苺に番号を付ける
now=1
for i in range(h):
    for j in range(w):
        if s[i][j]=='#':
            ans[i][j]=now
            now+=1
# 右に番号を着けていく
for i in range(h):
    for j in range(w-1):
        if ans[i][j+1]==0:
            ans[i][j+1]=ans[i][j]
# 左に番号を着けていく
for i in range(h):
    for j in range(w-1,0,-1):
        if ans[i][j-1]==0:
            ans[i][j-1]=ans[i][j]
# 下に番号を着けていく
for i in range(h-1):
    for j in range(w):
        if ans[i+1][j]==0:
            ans[i+1][j]=ans[i][j]
# ↑に番号を着けていく
for i in range(h-1,0,-1):
    for j in range(w):
        if ans[i-1][j]==0:
            ans[i-1][j]=ans[i][j]

for a in ans:
    print(*a)