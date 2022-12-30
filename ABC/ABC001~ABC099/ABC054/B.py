n,m=map(int,input().split())
a=[]
b=[]
for _ in range(n):
    a.append(list(input()))

for _ in range(m):
    b.append(list(input()))

d=0
r=0
while d<n-m+1 :
    for r in range(n-m+1):
        flg=0
        for i in range(m):
            for j in range(m):
                s=a[i+d][j+r]
                t=b[i][j]
                if s==t:
                    continue
                else:
                    flg+=1
        
        if flg==0:
            print('Yes')
            exit(0)

    d+=1


print('No')