n=int(input())
a=list(map(int,input().split()))

border_4 = n//2
border_2 = n

cnt_4=0
cnt_2=0

for i in range(n):
    if a[i]%4==0:
        cnt_4+=1
    elif a[i]%4!=0 and a[i]%2==0:
        cnt_2+=1
    else:
        continue


if cnt_4>=border_4:
    print('Yes')
elif n-cnt_4*2<=cnt_2:
    print('Yes')
else:
    print('No')