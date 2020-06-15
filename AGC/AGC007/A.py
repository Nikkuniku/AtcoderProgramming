h,w=map(int,input().split())
r=[]
for _ in range(h):
    a_i=input()
    r.append(a_i)

ans='Possible'
for i in range(h-1):
    for j in range(w-1):
        if r[i][j]=='#'and r[i][j+1]=='#' and r[i+1][j]=='#' and r[i+1][j+1]=='#':
            ans='Impossible'
        elif r[i][j]=='.' and r[i][j+1]=='#' and r[i+1][j]=='#' and r[i+1][j+1]=='#':
            ans='Impossible'
        elif r[i][j]=='#' and r[i][j+1]=='#' and r[i+1][j]=='#' and r[i+1][j+1]=='.':
            ans='Impossible'

print(ans)