h,w=map(int,input().split())
a=[]
b=[]

for _ in range(h):
    t=list(map(int,input().split()))
    a.append(t)
for _ in range(h):
    t=list(map(int,input().split()))
    b.append(t)

for i in range(h):
    for j in range(w):
        a[i][j]-=b[i][j]

ans=0
for i in range(h-1):
    for j in range(w-1):
        if a[i][j]!=0:
            ans+=abs(a[i][j])
            a[i+1][j]-=a[i][j]
            a[i][j+1]-=a[i][j]
            a[i+1][j+1]-=a[i][j]
            a[i][j]-=a[i][j]

for i in range(h):
    for j in range(w):
        if a[i][j]!=0:
            ans=-1
            break
        
if ans==-1:
    print('No')
    exit()
else:
    print('Yes')
    print(ans)