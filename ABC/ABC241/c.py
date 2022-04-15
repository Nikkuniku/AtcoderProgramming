n=int(input())
g=[]
for _ in range(n):
    g.append(list(input()))

# 横方向
ans='No'
for i in range(n):
    for j in range(n-5):
        cnt=0
        for k in range(6):
            if g[i][j+k]=='#':
                cnt+=1
        if cnt>=4:
            ans='Yes'
# 縦方向
for j in range(n):
    for i in range(n-5):
        cnt=0
        for k in range(6):
            if g[i+k][j]=='#':
                cnt+=1
        if cnt>=4:
            ans='Yes'

# 斜め方向(右下)
for i in range(n-5):
    for j in range(n-6,-1,-1):
        cnt=0
        for k in range(6):
            if g[i+k][j+k]=='#':
                cnt+=1
        if cnt>=4:
            ans='Yes'
# 斜め方向左下
for i in range(n-5):
    for j in range(5,n,1):
        cnt=0
        for k in range(6):
            if g[i+k][j-k]=='#':
                cnt+=1
        if cnt>=4:
            ans='Yes'

print(ans)