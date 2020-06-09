n=int(input())
p=list(map(int,input().split()))

flg =[0]*n

cnt=0
tmp=0
for i in range(n):
    if i<n-1 and p[i]==i+1:
        p[i],p[i+1] =p[i+1],p[i]
        cnt+=1
    if i==n-1 and p[i]==i+1:
        cnt+=1




print(cnt)
