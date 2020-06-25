n=int(input())
a=list(map(int,input().split()))

minus=[]
abses=[]
cnt=0
for i in range(n):
    if a[i]<0:
        minus.append(1)
    elif a[i]>0:
        minus.append(0)
    else:
        minus.append(0)
        cnt+=1
    abses.append(abs(a[i]))

if sum(minus)%2==0:
    print(sum(abses))
else:
    if cnt>0:
        print(sum(abses))
    else:
        print(sum(abses)- 2*min(abses))    