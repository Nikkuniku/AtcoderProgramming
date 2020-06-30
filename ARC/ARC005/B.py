x,y,w=input().split()
x,y=int(x),int(y)
c=[]
for _ in range(9):
    c.append(list(input()))
i=y-1
j=x-1
ans=[]
if w=='R':
    prev_i=i
    prev_j=j-1
    for _ in range(4):
        ans.append(c[i][j])
        if j<8:
            prev_j,j=j,2*j-prev_j
        else:
            prev_j,j=j,prev_j
elif w=='L':
    prev_i=i
    prev_j=j+1
    for _ in range(4):
        ans.append(c[i][j])
        if j>0:
            prev_j,j=j,2*j-prev_j
        else:
            prev_j,j=j,prev_j
        
elif w=='U':
    prev_i=i+1
    prev_j=j
    for _ in range(4):
        ans.append(c[i][j])
        if i>0:
            prev_i,i=i,2*i-prev_i
        else:
            prev_i,i=i,prev_i
elif w=='D':
    prev_i=i-1
    prev_j=j
    for _ in range(4):
        ans.append(c[i][j])
        if i<8:
            prev_i,i=i,2*i-prev_i
        else:
            prev_i,i=i,prev_i
elif w=='RU':
    prev_i=i+1
    prev_j=j-1
    for _ in range(4):
        ans.append(c[i][j])
        if i>0 and j<8:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,2*j-prev_j
        elif i>0 and j==8:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,prev_j
        elif i==0 and j<8:
            prev_i,i=i,prev_i
            prev_j,j=j,2*j-prev_j
        elif i==0 and j==8:
            prev_i,i=i,prev_i
            prev_j,j=j,prev_j
elif w=='RD':
    prev_i=i-1
    prev_j=j-1
    for _ in range(4):
        ans.append(c[i][j])
        if i<8 and j<8:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,2*j-prev_j
        elif i<8 and j==8:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,prev_j
        elif i==8 and j<8:
            prev_i,i=i,prev_i
            prev_j,j=j,2*j-prev_j
        elif i==8 and j==8:
            prev_i,i=i,prev_i
            prev_j,j=j,prev_j
elif w=='LU':
    prev_i=i+1
    prev_j=j+1
    for _ in range(4):
        ans.append(c[i][j])
        if i>0 and j>0:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,2*j-prev_j
        elif i>0 and j==0:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,prev_j
        elif i==0 and j>0:
            prev_i,i=i,prev_i
            prev_j,j=j,2*j-prev_j
        elif i==0 and j==0:
            prev_i,i=i,prev_i
            prev_j,j=j,prev_j
elif w=='LD':
    prev_i=i-1
    prev_j=j+1
    for _ in range(4):
        ans.append(c[i][j])
        if i<8 and j>0:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,2*j-prev_j
        elif i<8 and j==0:
            prev_i,i=i,2*i-prev_i
            prev_j,j=j,prev_j
        elif i==8 and j>0:
            prev_i,i=i,prev_i
            prev_j,j=j,2*j-prev_j
        elif i==8 and j==0:
            prev_i,i=i,prev_i
            prev_j,j=j,prev_j

num=''.join(ans)
print(num)