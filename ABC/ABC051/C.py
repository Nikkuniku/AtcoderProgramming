s_x,s_y,t_x,t_y=map(int,input().split())

ans=''

hor = t_x - s_x
ver = t_y - s_y

ans='U'*ver + 'R'*hor + 'D'*ver + 'L'*hor + 'L' + 'U'*(ver+1) +'R'*(hor+1)+'D'+'R' + 'D'*(ver+1)+'L'*(hor+1)+'U' 

print(ans)