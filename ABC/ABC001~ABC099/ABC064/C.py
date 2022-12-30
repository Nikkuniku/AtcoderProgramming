n=int(input())
a=list(map(int,input().split()))

rate = [1,400,800,1200,1600,2000,2400,2800]


color=[0]*8
free=0

for i in range(n):
    r=a[i]
    if 1<=r and r<=399:
        color[0]=1
    elif 400<=r and r<=799:
        color[1]=1
    elif 800<=r and r<=1199:
        color[2]=1
    elif 1200<=r and r<=1599:
        color[3]=1
    elif 1600<=r and r<=1999:
        color[4]=1
    elif 2000<=r and r<=2399:
        color[5]=1
    elif 2400<=r and r<=2799:
        color[6]=1
    elif 2800<=r and r<=3199:
        color[7]=1
    else:
        free+=1

num = sum(color)

ans_1 = num
#全員レート3200
if ans_1==0:
    ans_1=1

ans_2 = num+free


print(ans_1,ans_2)