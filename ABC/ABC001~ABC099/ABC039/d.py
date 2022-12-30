h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]

dx=[-1,-1,0,1,1,1,0,-1,0]
dy=[0,1,1,1,0,-1,-1,-1,0]

ans=[['.']*w for _ in range(h)]
can=False
for i in range(h):
    for j in range(w):
        around=True
        for k in range(9):
            nx=i+dx[k]
            ny=j+dy[k]
            if 0<=nx<h and 0<=ny<w:
                if s[nx][ny]=='.':
                    around=False
        if around:
            ans[i][j]='#'
            can=True
ans2=[['.']*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if ans[i][j]=='#':
            for k in range(9):
                nx=i+dx[k]
                ny=j+dy[k]
                if 0<=nx<h and 0<=ny<w:
                    ans2[nx][ny]='#'

answer='impossible'
if s==ans2:
    answer='possible'

print(answer)
if s==ans2:
    for c in ans:
        print(''.join(c))