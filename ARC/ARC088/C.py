x,y=map(int,input().split())

if y%2!=0:
    y-=1

cnt=0
while y>=x:
    cnt+=1
    y/=2

print(cnt)
