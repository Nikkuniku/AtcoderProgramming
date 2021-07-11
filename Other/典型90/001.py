n,l = map(int,input().split())
k=int(input())
a=[0]+list(map(int,input().split()))+[l]
yokan=[]

for i in range(1,len(a)):
    yokan.append(a[i]-a[i-1])

left = 0
right =2*l

while right - left >1:
    mid = (left+right)//2

    cnt=k
    tmp=0
    flg=0
    for i in range(len(yokan)):
        tmp +=yokan[i]
        if tmp>=mid and i < len(yokan)-1:
            cnt-=1
            if cnt>=0:
                tmp=0

    if cnt>0 or tmp<mid:
        flg+=1

    if flg==0:
        left=mid
    else:
        right=mid

print(left)
