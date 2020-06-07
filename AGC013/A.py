n=int(input())
a=list(map(int,input().split()))

if n<=2:
    print(1)
    exit(0)


flg=0
cnt=0
swi=0
for i in range(1,n):
    if swi==1:
        if a[i-1]==a[i]:
            flg==0
        elif a[i-1]<a[i]:
            flg=1
        elif a[i-1]>a[i]:
            flg=-1
        swi=0
        continue

    if a[i-1]<a[i]:
        if flg==-1:
            cnt+=1
            swi=1
        flg=1
    elif a[i-1]>a[i]:
        if flg ==1:
            cnt+=1
            swi=1
        flg=-1

print(cnt+1)