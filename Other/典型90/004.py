
h,w=map(int,input().split())
a=[]
for _ in range(h):
    a.append(list(map(int,input().split())))

# 行の和
cal1=[]
for i in range(h):
    p=sum(a[i])
    cal1.append(p)
# 列の和
cal2=[]
for i in range(w):
    q=0
    for j in range(h):
        q+=a[j][i]
        
    cal2.append(q)


ans=[[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        ans[i][j]=cal1[i]+cal2[j]
        ans[i][j]-=a[i][j]

for k in range(len(ans)):
    print(*ans[k])