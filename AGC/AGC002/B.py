n,m = map(int,input().split())

ball = [1]*n
d={}
for i in range(1,n+1):
    d[i]=0
d[1]=1

for _ in range(m):
    x,y = map(int,input().split())

    ball[x-1]-=1
    if d[x]==1:
        if ball[x-1]==0:
            d[x]=0
        d[y]=1
    ball[y-1]+=1

cnt=0
for _ ,v in d.items():
    if v==1:
        cnt+=1


print(cnt)